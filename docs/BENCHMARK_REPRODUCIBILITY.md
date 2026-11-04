# Reproducibilidad — MPI Matrix Benchmark

**Hallazgo:** `resultados.csv` incorpora texto de matrices dentro del mismo archivo que las cabeceras; no es una tabla limpia para análisis estadístico. Se preserva como evidencia histórica.

El archivo `examples/measurements-example.csv` contiene **datos ficticios**, exclusivamente para validar la herramienta. No representa ejecución MPI real.

## Protocolo mínimo de medición

1. Registrar CPU, RAM, sistema, versión MPI, compilador, flags y comandos.
2. Medir versiones secuencial y paralela con entradas idénticas y repetición de pruebas.
3. Exportar una fila por experimento con cabeceras exactas del validador.
4. Calcular speedup = tiempo secuencial / tiempo paralelo; eficiencia = speedup / número de procesos.
5. Publicar media o mediana y dispersión, junto con muestras brutas verificables.
6. Comparar resultados por tamaño de matriz y arquitectura; explicar sobrecarga de comunicación.

```bash
python scripts/validate_results.py examples/measurements-example.csv
python -m unittest discover -s tests -v
```

Una prueba del validador no demuestra rendimiento MPI. No atribuir los datos sintéticos a equipos ni a usuarios reales.