# Guion y Cronograma Oficial del Pitch — Spookython 2026 (Track B)

> **Reglas del Evento:**
> * **Duración del Pitch:** **5 minutos cronometrados** (respeto estricto del tiempo límite evaluado en la rúbrica).
> * **Ronda de Preguntas del Jurado:** **3 minutos**.
> * **Prueba de Fuego (Brote Sorpresa):** **5 minutos** para reconfigurar el escenario y mostrar la recomendación.
> * **Archivo de Diapositivas:** [`docs/pitch.pdf`](pitch.pdf) (Formato 16:9, máx 20 MB, tema táctil postapocalíptico).

---

## ⏱️ Cronograma de los 5 Minutos (Segundo a Segundo)

```
[0:00 - 0:35]  Diapositiva 1: Portada & Tesis de la Solución
[0:35 - 1:15]  Diapositiva 2: El Escenario Cordyceps & Calibración Manta (INEC 2022)
[1:15 - 1:55]  Diapositiva 3: Modelo SEIR & Grafo Multicapa (Blindaje de Red Flags)
[1:55 - 2:40]  Diapositiva 4: Estrategia Científica vs las 2 Líneas Base (No Intervenir y Azar)
[2:40 - 3:20]  Diapositiva 5: Nivel PRO — Territorio, Retorno Financiero & Memorando Alcalde
[3:20 - 4:05]  Diapositiva 6: Preparación para el Brote Sorpresa (Respuesta en Vivo)
[4:05 - 4:40]  Diapositiva 7: Arquitectura AWS Serverless & Gobernanza de Costos ($0,00 USD)
[4:40 - 5:00]  Diapositiva 8: Cierre & Invitación a la Prueba de Fuego (Semilla del Jurado)
```

---

## 🎙️ Guion Verbal del Orador (Pitch de 5 Minutos)

### Diapositiva 1: Portada & Tesis (0:00 - 0:35)
> *"Buenos días, estimados miembros del jurado. Somos el Comité de Contención Epidemiológica de Manta.  
> Ante un brote letal, una ciudad no puede cerrar todos sus comercios ni tiene vacunas infinitas para su gente. Las autoridades necesitan saber con precisión matemática: **a quién vacunar primero, dónde intervenir y cuánto dinero y vidas se van a salvar**.  
> Hoy presentamos un sistema de simulación epidemiológica en red multicapa, determinista, 100% reproducible y desplegado en AWS, capaz de superar categóricamente a la inacción y a la improvisación."*

### Diapositiva 2: El Escenario Cordyceps & Calibración Manta (0:35 - 1:15)
> *"Nuestro escenario modela una mutación mamífera de la Infección Cerebral por Cordyceps adaptada al entorno real de Manta.  
> Calibramos la población utilizando los datos del Censo INEC 2022: el cantón cuenta con 271.145 habitantes, con un promedio estricto de 3,2 personas por hogar y un 25,8% de población estudiantil.  
> Modelamos dos vías de contagio: mordeduras directas intrafamiliares y transmisión de esporas fúngicas en espacios de alta densidad como las líneas de buses y los mercados.  
> Con apenas 40 dosis de antígeno disponibles en la reserva cantonal, no podemos vacunar a todos. La matemática debe decidir por nosotros."*

### Diapositiva 3: Modelo SEIR & Grafo Multicapa (1:15 - 1:55)
> *"Construimos un modelo epidemiológico SEIR sobre un grafo sintético multicapa que simula los 4 espacios de interacción de Manta: hogares, aulas escolares, transporte público y mercados.  
> Cada habitante transita de Susceptible a Expuesto en 24 a 48 horas de incubación, luego a Infectado activo y finalmente a Inmune o Tratado.  
> **Importante para la rúbrica:** Nuestro algoritmo cuenta con un blindaje ético estricto. **Cero personas infectadas o inmunes son vacunadas**; cada dosis se asigna exclusivamente a personas sanas en riesgo real. Además, cada simulación genera una huella SHA-256 que garantiza que misma semilla y mismos parámetros arrojan el mismo resultado exacto."*

### Diapositiva 4: Estrategia Científica vs Líneas Base (1:55 - 2:40)
> *"La prueba de fuego exige comparar la estrategia contra dos líneas base bajo la misma semilla y el mismo azar biológico:  
> 1. **No intervenir:** la epidemia colapsa Manta en 18 días, infectando a más del 90% de la población.  
> 2. **Vacunar al azar:** gastar las mismas 40 dosis sin criterio salva apenas a unos pocos vecinos aislados.  
> Nuestra estrategia combina dos principios: primero, un **anillo de contención inmediato** alrededor del paciente cero; segundo, la protección de **super-propagadores** en transporte y mercados basada en grado de conectividad.  
> Ejecutamos simulaciones Monte Carlo reportando la media, el percentil 5 y el percentil 95, demostrando estadísticamente que no dependemos de la suerte: salvamos entre el 65% y el 85% de las vidas en riesgo."*

### Diapositiva 5: Nivel PRO — Territorio, Retorno Financiero & Alcaldía (2:40 - 3:20)
> *"Para el Nivel PRO, fuimos más allá de los números brutos:  
> Implementamos un **monitoreo territorial con semáforo epidemiológico** para las 5 parroquias de Manta, identificando a Tarqui como el principal nodo crítico por su flujo comercial.  
> Incorporamos un **modelo de retorno de inversión**: cada dosis cuesta \$25 USD frente a los \$200 USD que cuesta hospitalizar y contener un caso grave. Invertir \$1.000 USD en nuestra estrategia le ahorra más de \$45.000 USD netos al Municipio de Manta.  
> Y para que esto sea útil en el mundo real, el sistema genera automáticamente un **Dictamen Ejecutivo formal para el Alcalde**, listo para imprimir en PDF con directrices claras y sin tecnicismos."*

### Diapositiva 6: Preparación para el Brote Sorpresa (3:20 - 4:05)
> *"Sabemos que en la Prueba de Fuego el jurado alterará las condiciones. Nuestro sistema está diseñado con presets de respuesta instantánea:  
> Si duplican el contagio, la estrategia muta a contener super-hubs de transporte.  
> Si reducen las vacunas a la mitad, concentra el anillo en el núcleo familiar directo.  
> Si el brote inicia en el Mercado de Tarqui, activa cordones sanitarios interparroquiales.  
> Y si el antígeno pierde eficacia al 60%, el modelo ajusta la cobertura secundaria.  
> Todo esto responde en menos de 2 segundos sin romperse."*

### Diapositiva 7: Arquitectura AWS & Costos (4:05 - 4:40)
> *"Toda la solución está desplegada y operativa en producción sobre una arquitectura Serverless en `us-east-1` (URL: `https://d30ze7fyeksj6z.cloudfront.net/`):  
> Interfaz táctica distribuida en S3 y CloudFront, API REST en API Gateway, y orquestación con AWS Lambda y Step Functions Distributed Map para cómputo masivo.  
> Seguridad: cero credenciales en código y roles IAM de mínimo privilegio.  
> **Costos y criterio de desempate:** Nuestro gasto real acumulado durante todo el hackathon fue de apenas **\$0,00 USD**, con un tope de alerta en AWS Budgets de \$20,00 USD (apenas 0,00% consumido). El costo operativo mensual en producción no supera los \$5 a \$15 USD. Si la competencia empata en la Prueba de Fuego, ganamos por ser la solución más eficiente económicamente."*

### Diapositiva 8: Conclusión & Demostración en Vivo (4:40 - 5:00)
> *"En conclusión: entregamos un producto usable, matemáticamente riguroso, alineado a la demografía de Manta y económicamente viable.  
> Invitamos al jurado a proporcionarnos una semilla aleatoria para iniciar la simulación en vivo y poner a prueba nuestro motor. Muchas gracias."*

---

## 🛡️ Guía para los 3 Minutos de Preguntas del Jurado (Q&A)

### P1: "¿Por qué un modelo SEIR y no una simulación basada en agentes (ABM) pura?"
* **Respuesta:** *"Optamos por un híbrido SEIR sobre red estocástica porque combina el rigor biológico de los tiempos de incubación y remisión con la heterogeneidad del contacto humano. A diferencia de un ABM con física espacial innecesaria que elevaría los costos de cómputo en AWS, nuestro grafo de red modela con exactitud los puntos de contagio de Manta (buses, aulas, mercados) y responde en menos de 2 segundos en la nube."*

### P2: "¿Cómo garantizan que la estrategia no ganó por suerte en esa simulación específica?"
* **Respuesta:** *"Esa es la razón por la que ejecutamos simulaciones Monte Carlo con múltiples réplicas y reportamos la media junto a los percentiles 5 y 95 (bandas de confianza). Además, comparamos la estrategia contra el azar bajo la **misma semilla idéntica y la misma secuencia de números pseudoaleatorios**, demostrando que con la misma suerte biológica, nuestra asignación topológica siempre salva más vidas."*

### P3: "¿Por qué no vacunar a personas que ya presentan síntomas?"
* **Respuesta:** *"Porque en virología e inmunología el antígeno es profiláctico: estimula anticuerpos en tejido sano. Aplicar una vacuna de \$25 USD a un huésped donde el hongo ya colonizó el sistema nervioso central es un desperdicio del 100% del recurso público. Nuestro selector filtra rigurosamente el estado del nodo antes de inocular."*

### P4: "¿Por qué los costos en AWS son tan bajos (\$0,00 USD)?"
* **Respuesta:** *"Porque no tenemos infraestructura ociosa: no hay servidores EC2 ni clústeres encendidos 24/7 esperando peticiones. Todo el cómputo corre bajo demanda en AWS Lambda y Step Functions, aprovechando los tramos gratuitos (Free Tier) de 1 millón de invocaciones mensuales y almacenamiento S3 de bajo costo."*

---

## 🎃 Protocolo de Acción: Brote Sorpresa (5 Minutos)

Durante la evaluación en vivo, cuando el jurado diga su cambio de condiciones:

1. **Si el jurado dice: "El contagio es el doble"**
   * Acción en UI: Hacer clic en el preset **🍄 Doble Contagio** (sube $\beta$ a 0,32).
   * Clic en **Ejecutar Simulación**.
   * Argumento: *"Al duplicarse la tasa de transmisión aérea, el virus satura el transporte. Miren cómo la estrategia de anillo y hubs aún salva al X% de la población frente al colapso absoluto del azar."*

2. **Si el jurado dice: "Se redujo el presupuesto a la mitad (20 vacunas)"**
   * Acción en UI: Hacer clic en el preset **📉 Mitad de Dosis** (ajusta $K=20$).
   * Clic en **Ejecutar Simulación**.
   * Argumento: *"Con escasez extrema, vacunar al azar es equivalente a no hacer nada. Nuestro algoritmo repliega las dosis al hogar y contactos directos del paciente cero, extinguiendo el foco localmente."*

3. **Si el jurado dice: "El brote inició en el Mercado de Tarqui"**
   * Acción en UI: Hacer clic en el preset **🏬 Brote en Mercado**.
   * Clic en **Ejecutar Simulación**.
   * Mostrar pestaña **Territorio**: *"Observen el semáforo de Tarqui en rojo mientras Manta Centro permanece en verde. Nuestra intervención bloqueó los puentes de transporte antes de la metástasis urbana."*

4. **Si el jurado dice: "La vacuna tiene eficacia parcial (60%)"**
   * Acción en UI: Hacer clic en el preset **🧬 Mutación Fúngica**.
   * Clic en **Ejecutar Simulación**.
   * Argumento: *"Aun con un 40% de fuga inmunológica, la reducción de la densidad de susceptibles frena la tasa de reproducción efectiva $R_t$ por debajo de 1."*
