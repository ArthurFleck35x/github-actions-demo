import unittest
from hello_world import greet

class TestHelloWorld(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("GitHub Actions"), "Hello, GitHub Actions!")

if __name__ == '__main__':
    unittest.main()