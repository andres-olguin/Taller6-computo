"""Validador de datos tabulares MPI; no ejecuta cálculos paralelos."""
import argparse
import csv
import math
from pathlib import Path
import sys

COLUMNS = ["Procesos", "Tamano", "Tiempo_Secuencial", "Tiempo_Paralelo", "Speedup"]

def validate(source):
    reader = csv.DictReader(source)
    if not reader.fieldnames or [name.strip() for name in reader.fieldnames] != COLUMNS:
        raise ValueError("Cabeceras incorrectas.")
    valid = []
    for index, row in enumerate(reader, start=2):
        try:
            if None in row:
                raise ValueError("Columnas adicionales.")
            processes, size = int(row["Procesos"]), int(row["Tamano"])
            serial, parallel, reported = (float(row[name]) for name in COLUMNS[2:])
            if processes <= 0 or size <= 0 or any(not math.isfinite(value) or value <= 0 for value in (serial, parallel, reported)):
                raise ValueError("Valores fuera de rango.")
            calculated = serial / parallel
            if not math.isclose(reported, calculated, rel_tol=0.05):
                raise ValueError("Speedup inconsistente con los tiempos.")
        except (ValueError, TypeError) as exc:
            raise ValueError(f"Fila {index}: {exc}") from exc
        valid.append({"procesos": processes, "tamano": size, "speedup": calculated, "eficiencia": calculated / processes})
    if not valid:
        raise ValueError("Sin mediciones.")
    return valid

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=Path)
    args = parser.parse_args(argv)
    try:
        with args.file.open("r", encoding="utf-8-sig", newline="") as source:
            rows = validate(source)
        print(f"{len(rows)} filas válidas; última eficiencia: {rows[-1]['eficiencia']:.3f}")
        return 0
    except (OSError, UnicodeError, csv.Error, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
