"""Compara la estrategia contra no intervenir y contra el azar.

Cada corrida tiene su semilla hija. Dentro de la corrida, las tres políticas
usan el mismo paciente cero y la misma cinta aleatoria de contagios.
"""

from __future__ import annotations

import hashlib
import json

import numpy as np

from engine.config import Params
from engine.network import BARRIOS, build_city, describe_person, pool_for_locus
from engine.seir import apply_initial_state, simulate
from engine.strategies import compute_betweenness, pick_targets

POLICIES = ("estrategia", "azar", "nada")


def derive_seed(master: int, *parts: int) -> int:
    ss = np.random.SeedSequence([int(master) & 0x7FFFFFFF, *[int(p) & 0x7FFFFFFF for p in parts]])
    return int(ss.generate_state(1, dtype=np.uint32)[0])


def run_scenario(params: Params) -> dict:
    city = build_city(params.population, params.seed)
    betweenness = compute_betweenness(city) if params.criterio == "betweenness" else None

    per_policy_incidence: dict[str, list[int]] = {name: [] for name in POLICIES}
    per_policy_peak: dict[str, list[int]] = {name: [] for name in POLICIES}
    curve_sum = {name: np.zeros((params.days + 1, 4), dtype=np.float64) for name in POLICIES}
    zombie_runs = {name: [] for name in POLICIES}
    barrio_curves_sum = {name: np.zeros((params.days + 1, 5), dtype=np.float64) for name in POLICIES}
    barrio_inc_sum = {name: np.zeros(5, dtype=np.float64) for name in POLICIES}
    saved_vs_none: list[int] = []
    saved_vs_random: list[int] = []
    preview = None
    patient_zeros: list[int] = []

    for run in range(params.n_runs):
        run_seed = derive_seed(params.seed, 1000 + run)
        patient = _patient_zero(city, params, run_seed)
        patient_zeros.append(patient)
        transmission_seed = derive_seed(run_seed, 7)
        outcomes = {}
        for policy in POLICIES:
            targets = _targets(city, params, policy, patient, run_seed, betweenness)
            state, sus, weights = apply_initial_state(
                city.n,
                patient,
                targets,
                params.intervention if policy != "nada" else "vacuna",
                params.vaccine_efficacy if policy != "nada" else 1.0,
                city.edge_u,
                city.edge_v,
                city.weight,
                city.layer,
            )
            result = simulate(
                city.edge_u,
                city.edge_v,
                weights,
                city.n,
                params.days,
                params.beta,
                params.sigma,
                params.gamma,
                state,
                sus,
                transmission_seed,
                barrios=city.barrio,
            )
            outcomes[policy] = result
            per_policy_incidence[policy].append(result["incidence"])
            per_policy_peak[policy].append(result["peak_i"])
            curve_sum[policy] += result["hist"]
            zombie_runs[policy].append(result["hist"][:, 2].astype(np.float64))
            if "barrio_hist" in result and result["barrio_hist"] is not None:
                barrio_curves_sum[policy] += result["barrio_hist"]
                barrio_inc_sum[policy] += np.asarray(result["barrio_incidence"], dtype=np.float64)
            if policy == "estrategia" and preview is None:
                preview = [_person_out(city, node, betweenness) for node in targets[:12]]

        saved_vs_none.append(outcomes["nada"]["incidence"] - outcomes["estrategia"]["incidence"])
        saved_vs_random.append(outcomes["azar"]["incidence"] - outcomes["estrategia"]["incidence"])

    strategies = {}
    for policy in POLICIES:
        incidence = np.asarray(per_policy_incidence[policy], dtype=np.float64)
        peak = np.asarray(per_policy_peak[policy], dtype=np.float64)
        mean_curve = curve_sum[policy] / params.n_runs
        zombies = np.vstack(zombie_runs[policy])
        strategies[policy] = {
            "incidencia_media": _round(float(incidence.mean())),
            "incidencia_p05": _round(float(np.percentile(incidence, 5))),
            "incidencia_p95": _round(float(np.percentile(incidence, 95))),
            "pico_medio": _round(float(peak.mean())),
            "ataque_medio": _round(float(incidence.mean()) / city.n),
            "curvas": {
                "S": _series(mean_curve[:, 0]),
                "E": _series(mean_curve[:, 1]),
                "I": _series(mean_curve[:, 2]),
                "R": _series(mean_curve[:, 3]),
            },
            "zombies_p05": _series(np.percentile(zombies, 5, axis=0)),
            "zombies_p95": _series(np.percentile(zombies, 95, axis=0)),
        }

    saved_none = np.asarray(saved_vs_none, dtype=np.float64)
    saved_random = np.asarray(saved_vs_random, dtype=np.float64)
    base = strategies["nada"]["incidencia_media"]
    smart = strategies["estrategia"]["incidencia_media"]
    reduction = 0.0 if base <= 0 else (base - smart) / base

    # Nivel PRO: Análisis territorial de Manta por parroquias
    barrio_names = list(BARRIOS)
    barrio_pob = [int(np.sum(city.barrio == b)) for b in range(len(barrio_names))]
    mean_barrio_strat = barrio_curves_sum["estrategia"] / params.n_runs
    mean_barrio_nada = barrio_curves_sum["nada"] / params.n_runs
    mean_inc_strat = barrio_inc_sum["estrategia"] / params.n_runs
    mean_inc_nada = barrio_inc_sum["nada"] / params.n_runs

    barrio_resumen = []
    for b, bname in enumerate(barrio_names):
        pob = barrio_pob[b]
        inc_s = float(mean_inc_strat[b])
        inc_n = float(mean_inc_nada[b])
        salv_b = max(0.0, inc_n - inc_s)
        rate = inc_s / max(1, pob)
        riesgo = "Crítico" if rate > 0.35 else ("Alerta" if rate > 0.1 else "Controlado")
        barrio_resumen.append({
            "id": b,
            "nombre": bname,
            "poblacion": pob,
            "infectados_estrategia": _round(inc_s),
            "infectados_nada": _round(inc_n),
            "salvados": _round(salv_b),
            "tasa_ataque": _round(rate),
            "nivel_riesgo": riesgo,
        })

    territorial = {
        "barrios": barrio_resumen,
        "curvas_estrategia": {bname: _series(mean_barrio_strat[:, b]) for b, bname in enumerate(barrio_names)},
        "curvas_nada": {bname: _series(mean_barrio_nada[:, b]) for b, bname in enumerate(barrio_names)},
    }

    # Nivel PRO: Análisis de Costos y Presupuesto
    economia = _calcular_economia(params, strategies)

    comparacion = {
        "salvados_vs_nada_media": _round(float(saved_none.mean())),
        "salvados_vs_nada_p05": _round(float(np.percentile(saved_none, 5))),
        "salvados_vs_nada_p95": _round(float(np.percentile(saved_none, 95))),
        "salvados_vs_azar_media": _round(float(saved_random.mean())),
        "salvados_vs_azar_p05": _round(float(np.percentile(saved_random, 5))),
        "salvados_vs_azar_p95": _round(float(np.percentile(saved_random, 95))),
        "reduccion_vs_nada": _round(float(reduction)),
        "corridas_mejor_que_nada": int(np.sum(saved_none > 0)),
        "corridas_mejor_que_azar": int(np.sum(saved_random > 0)),
        "corridas": params.n_runs,
    }

    # Nivel PRO: Informe Ejecutivo para el Alcalde
    informe_ejecutivo = _informe_ejecutivo(params, comparacion, economia, barrio_resumen)

    payload = {
        "enfermedad": {
            "nombre": "Infección Cerebral por Cordyceps (CBI) — The Last of Us",
            "patogeno": "Ophiocordyceps unilateralis mutado (Hongo Cordyceps)",
            "vector": "Mordeduras directas de infectados (Runners/Clickers) y esporas en focos cerrados",
            "fases": "Sano -> Mordido/Esporas (~2 días) -> Infectado Activo -> Inmune/Tratado",
            "cura": "Antígeno fúngico / Inmunoterapia experimental (tipo Ellie) o cordón sanitario FEDRA",
        },
        "params": params.to_dict(),
        "red": city.summary,
        "dias": list(range(params.days + 1)),
        "estrategias": strategies,
        "comparacion": comparacion,
        "economia": economia,
        "territorial": territorial,
        "informe_ejecutivo": informe_ejecutivo,
        "recomendacion": _recomendacion(params, saved_none.mean(), reduction),
        "muestra_prioridad": preview or [],
        "pacientes_cero": patient_zeros,
        "leyenda": {
            "S": "Sano (No expuesto)",
            "E": "Mordido / Esporas (Incubación)",
            "I": "Infectado Cordyceps (Runners / Clickers)",
            "R": "Inmune / Tratado",
            "estrategia": _label(params),
            "azar": "Al azar, mismo presupuesto",
            "nada": "Sin intervención (Infección libre)",
        },
    }
    encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    payload["huella"] = hashlib.sha256(encoded.encode()).hexdigest()[:16]
    return payload


def run_one(params: Params, run: int) -> dict:
    """Una corrida Monte Carlo con las tres políticas. La usa la Lambda del mapa."""

    city = build_city(params.population, params.seed)
    betweenness = compute_betweenness(city) if params.criterio == "betweenness" else None
    run_seed = derive_seed(params.seed, 1000 + run)
    patient = _patient_zero(city, params, run_seed)
    transmission_seed = derive_seed(run_seed, 7)
    out: dict = {"run": run, "patient_zero": patient, "incidencias": {}, "picos": {}, "zombies": {}}
    for policy in POLICIES:
        targets = _targets(city, params, policy, patient, run_seed, betweenness)
        if policy == "nada":
            targets = []
        state, sus, weights = apply_initial_state(
            city.n,
            patient,
            targets,
            params.intervention if policy != "nada" else "vacuna",
            params.vaccine_efficacy if policy != "nada" else 1.0,
            city.edge_u,
            city.edge_v,
            city.weight,
            city.layer,
        )
        result = simulate(
            city.edge_u,
            city.edge_v,
            weights,
            city.n,
            params.days,
            params.beta,
            params.sigma,
            params.gamma,
            state,
            sus,
            transmission_seed,
        )
        out["incidencias"][policy] = result["incidence"]
        out["picos"][policy] = result["peak_i"]
        out["zombies"][policy] = result["hist"][:, 2].astype(int).tolist()
    return out


def _targets(city, params: Params, policy: str, patient: int, run_seed: int, betweenness):
    if policy == "nada":
        return []
    if policy == "azar":
        rng = np.random.default_rng(derive_seed(run_seed, 3))
        return pick_targets(city, params.vaccines, patient, "random", rng, betweenness)
    return pick_targets(city, params.vaccines, patient, params.criterio, None, betweenness)


def _patient_zero(city, params: Params, run_seed: int) -> int:
    if params.patient_zero != "aleatorio":
        return int(params.patient_zero) % city.n
    rng = np.random.default_rng(derive_seed(run_seed, 1))
    pool = pool_for_locus(city, params.locus)
    return int(rng.choice(pool))


def _person_out(city, node: int, betweenness) -> dict:
    data = describe_person(city, node)
    if betweenness is not None:
        data["betweenness"] = round(float(betweenness[node]), 4)
    return data


def _label(params: Params) -> str:
    criterio = {
        "puentes": "centralidad de puentes",
        "degree": "grado",
        "betweenness": "intermediación",
        "anillo": "anillo del caso y grado",
    }[params.criterio]
    if params.intervention == "cuarentena":
        return f"Cuarentena por {criterio}"
    return f"Vacunación por {criterio}"


def _recomendacion(params: Params, saved: float, reduction: float) -> str:
    recurso = "dosis" if params.intervention == "vacuna" else "aislamientos"
    acuerdo = "asignadas" if recurso == "dosis" else "asignados"
    if saved > 1:
        pct = reduction * 100
        pct_txt = f"{pct:.1f}" if pct >= 99 else f"{pct:.0f}"
        return (
            f"Con {params.vaccines} {recurso} {acuerdo} por {_criterio_corto(params.criterio)}, "
            f"se evitan en promedio {saved:.0f} contagios frente a no hacer nada "
            f"({pct_txt}% menos en la muestra). "
            f"Misma semilla {params.seed}, {params.n_runs} corridas."
        )
    if saved > 0:
        return (
            f"La estrategia apenas supera a no intervenir ({saved:.1f} personas). "
            "Conviene subir el presupuesto o bajar el contagio antes de confiar en el plan."
        )
    return (
        "Con estos parámetros la estrategia no supera a no intervenir. "
        "Revisa contagio, presupuesto, eficacia o el lugar del brote: el plan actual no se recomienda."
    )


def _criterio_corto(criterio: str) -> str:
    return {
        "puentes": "puentes entre grupos (bus, mercado, aulas)",
        "degree": "grado en la red",
        "betweenness": "intermediación",
        "anillo": "el hogar y los contactos del caso, y luego el grado",
    }[criterio]


def _series(values: np.ndarray) -> list[float]:
    return [round(float(v), 2) for v in values]


def _round(value: float) -> float:
    return round(float(value), 4)


def _calcular_economia(params: Params, strategies: dict) -> dict:
    unit_cost = 25.0 if params.intervention == "vacuna" else 15.0
    costo_intervencion = float(params.vaccines * unit_cost)
    costo_caso = 200.0  # Costo médico, descontaminación y contención de infectados/Clickers

    inc_strat = strategies["estrategia"]["incidencia_media"]
    inc_azar = strategies["azar"]["incidencia_media"]
    inc_nada = strategies["nada"]["incidencia_media"]

    costo_sanitario_nada = inc_nada * costo_caso
    costo_sanitario_azar = inc_azar * costo_caso
    costo_sanitario_estrategia = inc_strat * costo_caso

    costo_total_nada = costo_sanitario_nada
    costo_total_azar = costo_sanitario_azar + costo_intervencion
    costo_total_estrategia = costo_sanitario_estrategia + costo_intervencion

    ahorro_vs_nada = max(0.0, costo_total_nada - costo_total_estrategia)
    ahorro_vs_azar = max(0.0, costo_total_azar - costo_total_estrategia)
    roi = (ahorro_vs_nada / costo_intervencion) if costo_intervencion > 0 else 0.0

    return {
        "costo_unitario": unit_cost,
        "inversion_intervencion": round(costo_intervencion, 2),
        "costo_sanitario_caso": costo_caso,
        "costo_total_estrategia": round(costo_total_estrategia, 2),
        "costo_total_azar": round(costo_total_azar, 2),
        "costo_total_nada": round(costo_total_nada, 2),
        "ahorro_vs_nada": round(ahorro_vs_nada, 2),
        "ahorro_vs_azar": round(ahorro_vs_azar, 2),
        "roi_estimado": round(roi, 2),
    }


def _informe_ejecutivo(params: Params, comp: dict, econ: dict, territorial: list[dict]) -> dict:
    salvados = comp["salvados_vs_nada_media"]
    reduccion = comp["reduccion_vs_nada"] * 100
    ahorro = econ["ahorro_vs_nada"]
    inversion = econ["inversion_intervencion"]
    foco = max(territorial, key=lambda x: x["infectados_nada"]) if territorial else {"nombre": "Tarqui"}

    return {
        "destinatario": "Alcalde del Cantón Manta y Comité de Operaciones de Emergencia (COE)",
        "asunto": "Dictamen de Contención Epidemiológica: Infección Cerebral por Cordyceps (CBI)",
        "diagnostico": (
            f"Brote activo de Infección Cerebral por Cordyceps (CBI / The Last of Us) detectado en la ciudad. "
            f"El mayor riesgo de propagación descontrolada se localiza en la parroquia {foco['nombre']} "
            "debido a la densidad de puestos de mercado y transporte colectivo."
        ),
        "impacto_estrategia": (
            f"El despliegue de {params.vaccines} dosis/medidas mediante estrategia de {_criterio_corto(params.criterio)} "
            f"logra salvar a {salvados:.0f} personas en la muestra ({reduccion:.1f}% de reducción frente a no intervenir). "
            f"Supera contundentemente a la distribución aleatoria en {comp['corridas_mejor_que_azar']}/{comp['corridas']} corridas Monte Carlo."
        ),
        "analisis_financiero": (
            f"Con una inversión municipal estimada de ${inversion:,.2f} USD, se previene un daño sanitario y logístico de "
            f"${ahorro:,.2f} USD en emergencias por infectados/Clickers (Retorno de Inversión estimado: {econ['roi_estimado']:.1f}x)."
        ),
        "directrices_inmediatas": [
            "1. Inmunizar o aislar de inmediato el anillo de contactos familiares y directos del paciente cero.",
            f"2. Proteger a los comerciantes y transportistas clave en {foco['nombre']} para bloquear la dispersión de esporas.",
            "3. Establecer reserva estratégica ante posibles brotes de esporas masivos (Brote Sorpresa).",
        ],
        "conclusion": (
            "Se aconseja adoptar de manera perentoria esta estrategia de contención focalizada "
            "para evitar la saturación y colapso del cantón Manta."
        ),
    }

