# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Equipos participantes y jurado del hackathon Spookython 2026, Track B. Los usan en una demo en vivo o revisión asíncrona desde un navegador de escritorio; el jurado además ejecuta "brotes sorpresa" con parámetros alterados para probar la robustez del motor y del criterio de asignación.

## Product Purpose

Simula día a día un brote de Cordyceps (CBI) sobre una red de contactos sintética de Manta y compara la estrategia de contención contra dos líneas base bajo la misma semilla: no intervenir y gastar el mismo presupuesto al azar. El éxito es que cualquier persona pueda ejecutar el escenario, entender el dictamen y verificar que el resultado es determinista y reproducible.

## Positioning

Un motor SEIR determinista y auditable con estrategia de asignación en anillo y grado, comparación obligatoria contra dos líneas base, huella SHA-256 y lectura territorial por parroquias; todo corre localmente sin nube ni dependencias de frontend.

## Operating Context

Ejecución local con `python run.py`, que sirve la UI en `http://127.0.0.1:8000/`. La demo dura pocos minutos e incluye cambiar parámetros, lanzar Monte Carlo y presentar el informe ejecutivo. También existe una SPA React alternativa en `frontend/` que no es la superficie de esta iteración.

## Capabilities and Constraints

- Parámetros: semilla, población de muestra, días, β, σ, γ, dosis K, eficacia, epicentro, paciente cero, corridas Monte Carlo, criterio de asignación e intervención.
- Vistas: resumen con KPIs y curvas, avance territorial por las 5 parroquias de Manta, lista prioritaria de vacunación, informe ejecutivo para el Alcalde y ficha biológica del Cordyceps.
- Presets de brote sorpresa: doble contagio, mitad de dosis, brote en mercado y mutación fúngica.
- Restricción dura: ninguna persona infectada o inmune puede recibir dosis.
- Restricción de esta iteración: preservar todos los IDs, funciones, pestañas y textos existentes; el cambio es de piel y jerarquía visual.
- No hay generación de imágenes ni assets fotográficos en el proyecto.

## Brand Commitments

El escenario está inspirado en *The Last of Us* (Cordyceps CBI, FEDRA, zonas de cuarentena, Runners/Clickers, inmunidad tipo Ellie) y el tono del evento es una simulación seria de comité epidemiológico, no un juego. La paleta es libre para esta iteración.

## Evidence on Hand

Datos de referencia citados en el README: INEC Censo 2022 (Manta, 271.145 habitantes; 3,2 personas por hogar), parámetros epidemiológicos calibrados y resultados generados por el motor. No existen testimonios, clientes ni métricas de producción; no deben fabricarse.

## Product Principles

1. La legibilidad del dato manda: el tema nunca puede ocultar una cifra, un estado ni una acción.
2. Toda afirmación se demuestra con la simulación, no con adjetivos.
3. La reproducibilidad es visible: semilla, muestra y huella siempre a la vista.
4. La ficción da el tono, la epidemiología da la verdad.
5. La demo debe entenderse en segundos y sobrevivir a un brote sorpresa.

## Accessibility & Inclusion

Contraste de texto ≥4.5:1, foco de teclado visible, controles nativos utilizables y navegación por pestañas comprensible sin depender solo del color.
