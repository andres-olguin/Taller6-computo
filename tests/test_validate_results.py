import io
import unittest
from scripts.validate_results import validate

HEADER = "Procesos,Tamano,Tiempo_Secuencial,Tiempo_Paralelo,Speedup\n"

class BenchmarkValidationTests(unittest.TestCase):
    def test_valid_result(self):
        values = validate(io.StringIO(HEADER + "4,500,10,5,2\n"))
        self.assertEqual(values[0]["eficiencia"], 0.5)

    def test_invalid_speedup(self):
        with self.assertRaises(ValueError):
            validate(io.StringIO(HEADER + "4,500,10,5,4\n"))

    def test_malformed_legacy_format(self):
        with self.assertRaises(ValueError):
            validate(io.StringIO(HEADER + "Matriz A:\n"))

if __name__ == "__main__":
    unittest.main()
