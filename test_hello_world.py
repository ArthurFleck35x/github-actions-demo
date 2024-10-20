import unittest
from hello_world import greet

class TestHelloWorld(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("GitHub Actions"), "Hello, GitHub Actions!")

if __name__ == '__main__':
    unittest.main()

# importieren des unittest Moduls und der greet Funktion aus der hello_world.py
# Testklasse, erbt von unittest.TestCase und initialisierung einer Methode, die einen String mit dem Ausgabestring von greet überprüft
# Testausführung starten
