"""Lanzador directo de la interfaz web para el objetivo del proyecto.

Spookython 2026 — Track B: La Plaga Zombie (Cordyceps CBI - The Last of Us)
Comité de Contención de Manta.
"""

import os
import socket
import sys
import threading
import time
import webbrowser

# Reconfigurar stdout para UTF-8 si está disponible en Windows
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Asegurar que src esté en el PYTHONPATH
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)


def open_browser(url: str, delay: float = 1.0):
    time.sleep(delay)
    try:
        webbrowser.open(url)
    except Exception as exc:
        print(f"[!] No se pudo abrir el navegador automáticamente: {exc}")


def find_available_port(host: str = "127.0.0.1", preferred: int = 8000) -> int:
    env_port = os.environ.get("PORT")
    if env_port:
        try:
            return int(env_port)
        except ValueError:
            pass
    for p in [preferred, 8080, 8001, 8002, 8888]:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind((host, p))
                return p
            except OSError:
                continue
    return preferred


def main():
    import uvicorn

    host = "127.0.0.1"
    port = find_available_port(host, 8000)
    url = f"http://{host}:{port}/"

    banner = rf"""
==========================================================================
 [BIOHAZARD] SPOOKYTHON 2026 · TRACK B · LA PLAGA ZOMBIE
 [PATOGENO]  Infeccion Cerebral por Cordyceps (CBI) - The Last of Us
 [ESCENARIO] Red de Contactos de Manta (Censo INEC 2022)
 [ESTRATEGIA] Vacunacion en Anillo vs Azar vs Sin Intervencion
==========================================================================
 [OK] Servidor API & UI activo en: {url}
 [OK] Abriendo interfaz grafica en tu navegador predeterminado...
 
 Presiona Ctrl + C para detener el servidor.
==========================================================================
"""
    print(banner)

    # Abrir navegador tras levantar el servidor
    threading.Thread(target=open_browser, args=(url,), daemon=True).start()

    uvicorn.run("api.main:app", host=host, port=port, log_level="info")


if __name__ == "__main__":
    main()
