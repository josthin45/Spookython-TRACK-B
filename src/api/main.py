from pathlib import Path

from fastapi import Body, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse, HTMLResponse

from engine.compare import run_scenario
from engine.config import Params, parse_params

STATIC_INDEX = Path(__file__).resolve().parent / "static" / "index.html"

app = FastAPI(
    title="Comité de Contención — Manta",
    version="0.2.0",
    summary="Simulador SEIR de la plaga Cordyceps (CBI) sobre la red de contactos de Manta.",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
@app.get("/app", response_class=HTMLResponse)
def index() -> FileResponse:
    if STATIC_INDEX.exists():
        return FileResponse(STATIC_INDEX)
    return HTMLResponse("<h1>UI no encontrada</h1>", status_code=404)


@app.get("/health")
def health() -> dict:
    return {"ok": True, "servicio": "motor-local"}


@app.get("/defaults")
def defaults() -> dict:
    return Params().to_dict()


@app.post("/simulate")
def simulate(body: dict = Body(...)) -> dict:
    try:
        params = parse_params(body)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return run_scenario(params)
