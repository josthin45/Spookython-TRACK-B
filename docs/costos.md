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
| **Nombre del Presupuesto** | Presupuesto activo en la consola de AWS Budgets | `spookython-mensual` |
| **Fecha de inicio del presupuesto** | Apertura del ciclo de monitoreo mensual | 2026-10-01 |
| **Fecha de corte y entrega** | Corte previo a la entrega y demo final | 27 de octubre de 2026 |
| **Gasto Real Acumulado (MTD)** | Importe gastado total confirmado por AWS Budgets (`Actual frente a presupuestado`) | **\$0,00 USD** |
| **Tope Presupuestado (Budget Alert)** | Límite mensual configurado — `MonthlyBudgetUsd` | **\$20,00 USD** |
| **Porcentaje de Presupuesto Consumido** | Relación entre gasto real y tope de seguridad | **0,00% consumido** |
| **Estado del Presupuesto** | Semáforo de salud del presupuesto AWS | ✅ **En buen estado** |
| **Alertas configuradas** | Umbral activo con notificación a `pilozocesar@gmail.com` (verificado) | 2 alertas activas |
| **Tipo de presupuesto** | Modalidad de facturación | Presupuesto de costos mensual recurrente |
| **Captura del Presupuesto** | Evidencia visual de la consola de AWS Budgets | [`docs/budget.png`](budget.png) |

> **Nota de Gobernanza de Costos y Criterio de Desempate:**
> El sistema se diseñó 100% Serverless con cobro por uso (*pay-as-you-go*) y sin aprovisionamiento de capacidad fija (cero EC2, cero NAT Gateways, cero bases de datos RDS con cobro por hora). Durante el evento, el gasto real acumulado fue de **\$0,00 USD** — completamente cubierto por el AWS Free Tier — con un tope de alerta activo en **\$20,00 USD** desde el primer día. Ante el criterio de desempate de la rúbrica oficial (*"Gana el equipo con mejor nota en la Prueba de Fuego. Si persiste el empate, gana el de menor costo declarado"*), la solución presenta el menor costo posible declarado: **cero dólares facturados**, con un costo mensual operativo proyectado en régimen de apenas **\$5 a \$15 USD** bajo carga real.
