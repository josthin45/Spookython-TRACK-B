# Costos — Spookython 2026 Track B

Región: **us-east-1**. Estimado de un mes de evento, no de un servicio siempre encendido.
No hay EC2, NAT Gateway, RDS ni balanceadores. Todo es pago por uso.

## Qué queda prendido

| Pieza | Uso previsto en el evento | Estimado mensual |
| --- | --- | --- |
| Lambda orquestador | Demo en vivo y ensayos. ~2.000 invocaciones de 2 s a 1,7 GB | < 1 USD |
| Lambda simulador + agregador | Solo si se dispara el mapa. Tope de 20 en paralelo | < 2 USD si se usa con moderación |
| Step Functions Distributed Map | Nivel Pro. Cada corrida son pocos estados. Concurrencia 20 | < 3 USD bajo el tope de 400 corridas por trabajo |
| API Gateway REST | Las mismas ~2.000 llamadas | < 1 USD |
| CloudFront + S3 frontend | Tráfico del jurado y del equipo | < 1 USD |
| S3 resultados | JSON de trabajos. Se borra a los 14 días | < 1 USD |
| DynamoDB on-demand | Un ítem por trabajo | < 1 USD |
| CloudWatch Logs | Retención 7 días | 1–2 USD |
| AWS Budgets | Dos notificaciones (50% real, 100% previsto). Los dos primeros presupuestos con acción suelen entrar en el tramo gratuito; si no, unos céntimos al día | < 2 USD |
| **Total de referencia** | | **5 a 15 USD** |

El tope de la plantilla es **20 USD** (`MonthlyBudgetUsd`). La alerta sale al 50% del gasto real y cuando el pronóstico llega al 100%.

## Qué haría subir la cuenta

- Subir `BATCH_MAX_RUNS` y lanzar miles de mapas sin el tope de concurrencia.
- Dejar la retención de logs en “nunca expira”.
- Crear un NAT Gateway o una instancia “para probar”. No hace falta para este diseño.
- Pedir intermediación (`betweenness`) en poblaciones grandes dentro de un bucle de ensayos: es más lento, no más caro por sí solo, pero alarga el tiempo de Lambda.

## Gasto real del evento

Monitoreo y corte de costos durante el desarrollo, despliegue y pruebas del hackathon (Spookython 2026).

| Concepto | Detalle / Métrica | Valor Registrado |
| --- | --- | --- |
| **Fecha de inicio / Despliegue del stack** | Creación del stack `spookython` en AWS SAM (`us-east-1`) | 26 de octubre de 2026 |
| **Fecha de corte y entrega** | Corte previo a la entrega y demo final | 27 de octubre de 2026 |
| **AWS Lambda** | Pruebas locales y ejecuciones en la nube (~650 invocaciones de test) | \$0,00 USD (Cubierto por AWS Free Tier: 1M gratis) |
| **Amazon API Gateway** | Pruebas de integración HTTP REST (`/api/simulate`, `/health`) | \$0,01 USD (Fracción de centavo) |
| **Amazon S3 & CloudFront** | Hosting estático de la SPA en CloudFront (`https://d30ze7fyeksj6z.cloudfront.net/`) y S3 | \$0,02 USD (Tráfico bajo en pruebas de equipo) |
| **Amazon DynamoDB** | Modo On-Demand (lecturas/escrituras puntuales de prueba) | \$0,00 USD (Dentro de los 25 GB / WCU gratuitos) |
| **AWS Step Functions** | Ensayos de Distributed Map para Monte Carlo | \$0,04 USD (Dentro del Free Tier de transiciones) |
| **Amazon CloudWatch Logs** | Ingesta de métricas y logs de funciones Lambda (retención 7 días) | \$0,05 USD |
| **AWS Budgets** | Alerta configurada para \$20 USD a `pilozocesar@gmail.com` | \$0,00 USD (Primeros 2 presupuestos mensuales gratis) |
| **Gasto Real Acumulado del Evento** | Total facturado según AWS Billing / Cost Management | **\$0,12 USD** |
| **Tope Presupuestado (Budget Alert)** | Límite mensual configurado en CloudFormation / SAM | **\$20,00 USD** |
| **Porcentaje de Presupuesto Consumido** | Relación entre gasto real y tope de seguridad | **0,6% consumido** |
| **Captura del Presupuesto** | Evidencia visual requerida por las bases del evento | [`docs/budget.png`](budget.png) |

> **Nota de Gobernanza de Costos y Criterio de Desempate:**
> El sistema se diseñó 100% Serverless con cobro por uso (*pay-as-you-go*) y sin aprovisionamiento de capacidad fija (cero EC2, cero NAT Gateways, cero bases de datos RDS con cobro por hora). Esto garantiza que durante el evento el gasto acumulado no superó los \$0,15 USD, y que ante el criterio de desempate de la rúbrica oficial (*"Gana el equipo con mejor nota en la Prueba de Fuego. Si persiste el empate, gana el de menor costo declarado"*), la solución mantiene una ventaja competitiva máxima con un costo proyectado mensual operativo de apenas **\$5 a \$15 USD** bajo carga regular.
