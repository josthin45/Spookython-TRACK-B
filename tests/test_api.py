from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_health_y_defaults():
    health = client.get("/health")
    assert health.status_code == 200
    assert health.json()["ok"] is True
    defaults = client.get("/defaults")
    assert defaults.status_code == 200
    assert defaults.json()["seed"] == 42


def test_simular_es_reproducible_por_http():
    body = {"seed": 5, "n_runs": 2, "population": 120, "days": 12, "vaccines": 8}
    first = client.post("/simulate", json=body)
    second = client.post("/simulate", json=body)
    assert first.status_code == 200
    assert first.json()["huella"] == second.json()["huella"]
    assert "recomendacion" in first.json()


def test_rechaza_contagio_imposible():
    response = client.post("/simulate", json={"beta": 5})
    assert response.status_code == 400
    assert "beta" in response.json()["detail"]


def test_interfaz_web_sirve_html():
    response = client.get("/")
    assert response.status_code == 200
    assert "Cordyceps" in response.text
    assert "Manta" in response.text


def test_simular_incluye_cordyceps_territorio_y_economia():
    body = {"seed": 42, "n_runs": 2, "population": 100, "days": 10, "vaccines": 10}
    response = client.post("/simulate", json=body)
    assert response.status_code == 200
    data = response.json()
    assert "enfermedad" in data
    assert "Cordyceps" in data["enfermedad"]["nombre"]
    assert "economia" in data
    assert data["economia"]["ahorro_vs_nada"] >= 0
    assert "territorial" in data
    assert len(data["territorial"]["barrios"]) == 5
    assert "informe_ejecutivo" in data
    assert "Alcalde" in data["informe_ejecutivo"]["destinatario"]
