import unittest

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

class TestFactorial(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(120, factorial(5))

if __name__ == '__main__':
    unittest.main()
