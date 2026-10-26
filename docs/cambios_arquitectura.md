# Bitácora de Cambios Técnicos y Alineación de Arquitectura

**Proyecto:** Spookython 2026 — Track B: La Plaga Zombie (Escenario Manta)  
**Patógeno Modelado:** Infección Cerebral por Cordyceps (CBI) — *The Last of Us*  
**Fecha:** 26 de octubre de 2026  

---

## 1. Motivación y Objetivo de los Cambios

El objetivo fue completar los requisitos del Track B (Nivel Base + Nivel PRO) e integrar la temática solicitada (**el virus/hongo Cordyceps de The Last of Us**), resolviendo la necesidad de una **interfaz gráfica directa (UI)** ejecutable en local sin fricción ni dependencias adicionales, manteniendo intacta la compatibilidad con la arquitectura serverless en AWS.

---

## 2. Mapa Detallado de Archivos Modificados y Creados

```
MODIFICADOS:
├── src/engine/seir.py         -> Soporte para conteo territorial de infectados por parroquia
├── src/engine/compare.py      -> Métricas territoriales, modelo económico, informe para alcalde y metadatos Cordyceps
├── src/api/main.py            -> Servicio de UI HTML directa en / y /app
├── frontend/src/types.ts      -> Sincronización de tipos TypeScript para el escenario Cordyceps
├── frontend/src/App.tsx       -> Actualización de textos, títulos y leyendas temáticas
├── tests/test_api.py          -> Tests para verificación de la UI servida y payload extendido
└── README.md                  -> Documentación completa del proyecto y guía de ejecución

CREADOS:
├── run.py                     -> Script lanzador directo con detección de navegador y encoding seguro
├── src/api/static/index.html  -> UI interactiva completa (SPA vanilla en HTML/CSS/JS moderno)
└── docs/cambios_arquitectura.md -> Este documento técnico
```

---

## 3. Principio de Cero Conflictos y Aislamiento de Capas

Para asegurar que los cambios no rompan la arquitectura ni generen conflictos entre componentes:

1. **El Motor Epidemiológico (`src/engine`) es Python Puro:**
   * No tiene dependencias de AWS SDK (`boto3`).
   * No requiere conexión a internet ni bases de datos.
   * `seir.py` acepta `barrios: np.ndarray | None = None` como parámetro opcional. Si las Lambdas de AWS llaman a `simulate` sin `barrios`, la función opera con 100% de retrocompatibilidad.
2. **Compatibilidad con las Lambdas de AWS (`src/lambdas`):**
   * El orquestador síncrono (`lambdas/orchestrator/handler.py`) consume `run_scenario()`. Como `run_scenario()` devuelve un diccionario enriquecido manteniendo todas las claves preexistentes (`params`, `red`, `dias`, `estrategias`, `comparacion`, `recomendacion`, `huella`), la respuesta HTTP en API Gateway es idéntica y válida.
   * El simulador de mapa distribuido (`lambdas/simulator/handler.py`) y el agregador (`lambdas/aggregator/handler.py`) continúan operando sin modificaciones.
3. **Doble Vía para la UI (Local Directa vs React SPA):**
   * **Vía Directa (Recomendada):** `src/api/static/index.html` servido por FastAPI mediante `python run.py`. Elimina el bloqueo por falta de Node.js en la máquina del usuario o del jurado.
   * **Vía React/Vite:** Los archivos en `frontend/` se actualizaron para que, si se compila para CloudFront/S3 con `npm run build`, la SPA React cuente con los mismos tipos y consistencia temática.
4. **Reproducibilidad Criptográfica Garantizada:**
   * La huella (`huella`) generada por SHA-256 sigue siendo una función puramente determinista del payload. Dos ejecuciones con los mismos parámetros y semilla producen el mismo hash exacto.

---

## 4. Desglose de Funcionalidades Implementadas

### A. Enfermedad: Cordyceps Brain Infection (The Last of Us)
* **Vector:** Mordedura directa intrafamiliar (peso 1.0) y esporas fúngicas en transporte público (buses de Manta) y recintos densos (mercados).
* **Parámetros SEIR Calibrados:**
  * $\sigma = 0.50$: Incubación de ~2 días antes de la manifestación de agresividad y pérdida de control motor.
  * $\gamma = 0.25$: Fase infecciosa de ~4 días (Runners / Clickers) hasta neutralización sanitaria o aislamiento.
  * $\beta = 0.16$: Tasa de transmisión seleccionada para permitir la ventana de intervención antes del escape descontrolado.
  * Eficacia: Inmunoterapia fúngica con protección total (tipo Ellie) o parcial (60% en brote sorpresa).

### B. Módulo Territorial de Manta (Nivel PRO)
* Desglose por las 5 parroquias reales del modelo sintético:
  1. **Manta (Centro):** Densidad media, oficinas y conectividad.
  2. **Tarqui:** Epicentro comercial crítico, contiene el Mercado de Tarqui con alto grado de conexiones.
  3. **Eloy Alfaro:** Zona residencial periférica conectada por rutas de bus.
  4. **San Mateo:** Zona costera y pesquera.
  5. **San Lorenzo:** Parroquia rural del cantón.
* Semáforo de riesgo dinámico (*Controlado*, *Alerta*, *Crítico*) y gráfica comparativa de barras para el avance de infectados con estrategia vs inacción.

### C. Modelo Económico y Presupuestario (Nivel PRO)
* Costo por dosis de antígeno/vacuna: **\$25.00 USD**.
* Costo por aislamiento/cuarentena: **\$15.00 USD**.
* Costo de respuesta sanitaria, descontaminación y contención por cada infectado: **\$200.00 USD**.
* Retorno de Inversión (ROI):
  $$\text{ROI} = \frac{\text{Ahorro en daños sanitarios} - \text{Inversión en dosis}}{\text{Inversión en dosis}}$$

### D. Memorando para el Alcalde (Nivel PRO)
* Dictamen formal para el Alcalde de Manta y el COE Cantonal con 6 secciones claras:
  1. Destinatario y Asunto oficial.
  2. Diagnóstico territorial del brote.
  3. Cuantificación de vidas salvadas (media y percentiles p5–p95).
  4. Balance de costos e inversión pública.
  5. Tres directrices operativas perentorias.
  6. Conclusión y recomendación final del Comité.

### E. Presets de la Prueba de Fuego (Brote Sorpresa)
* Ensayos inmediatos en vivo con un clic para responder al jurado en menos de 5 minutos:
  * **🍄 Doble Contagio:** Simula esporas densas ($\beta \times 2$).
  * **📉 Mitad de Dosis:** Simula retraso logístico de antígenos ($K/2$).
  * **🏬 Brote en Mercado:** Foco inicial en Tarqui.
  * **🧬 Mutación Fúngica:** Eficacia de vacuna al 60%.

---

## 5. Verificación de Calidad

* **Pruebas Automatizadas:** 18 pruebas unitarias en `python -m pytest` pasando satisfactoriamente:
  * Pruebas de API (`test_api.py`): 5 pruebas.
  * Pruebas de motor SEIR y reproducibilidad (`test_engine.py`): 9 pruebas.
  * Pruebas de handlers AWS (`test_handlers.py`): 4 pruebas.
* **Seguridad y Costos:**
  * Cero credenciales hardcodeadas.
  * Plantilla AWS SAM protegida por alertas de AWS Budgets a \$20 USD/mes.
