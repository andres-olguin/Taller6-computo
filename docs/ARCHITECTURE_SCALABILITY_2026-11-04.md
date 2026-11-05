# mpi-matrix-benchmark — Ingeniería, pruebas y escalabilidad realista

**Estado:** plan técnico documentado el 04-11-2026. No constituye resultado experimental ejecutado.

## Evidencia de partida

Implementación de multiplicación matricial C++/MPI y archivo resultados.csv que mezcla texto de matrices con cabeceras; existe validador CSV y ejemplos ficticios.

## Incrementos de ingeniería

Conservar baseline secuencial; fijar matriz y semilla, tamaño de problema, número de procesos, afinidad CPU y flags. Registrar al menos varias repeticiones y dispersión; generar resultados con origen real etiquetado.

## Estrategia de escalabilidad

Aumentar N y procesos solo si memoria y hardware lo permiten; medir tiempo de transferencia, cómputo, speedup/eficiencia. Evaluar memoria NUMA y tamaño de matriz antes de discutir cluster/HPC.

## Riesgos y condición de aprobación

No convertir ejemplo sintético en medición; no anunciar escalamiento lineal sin datos. CI del validador no demuestra rendimiento del algoritmo MPI.

## Protocolo de experimentación y calidad

Cada comparativa debe incluir referencia de código/commit, entorno, versiones, semilla cuando corresponda, entrada reproducible, comando de ejecución, datos brutos, repetición y límites. Separar datos de ejemplo de resultados realmente ejecutados. Mantener código histórico y coautoría intactos; publicar evidencias de tests de CI y pruebas manuales en su contexto, sin inventar métricas.

## Referencias consultadas (2026-11-04)

- [AWS Well-Architected — rendimiento y costo](https://docs.aws.amazon.com/wellarchitected/).
- [NIST SSDF — prácticas seguras de software](https://csrc.nist.gov/pubs/sp/800/218/final).
- [Google SRE — medición y objetivos](https://sre.google/workbook/implementing-slos/).

Las referencias son metodológicas; no corroboran los benchmarks particulares de este repositorio.
