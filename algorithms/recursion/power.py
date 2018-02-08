import unittest

def power(x, n):
    """Compute the value x ** n for integer n."""
    if n == 0:
        return 1
    else:
        partial = power(x, n // 2)      # rely on truncated division
        result = partial * partial
        if n % 2 == 1:                  # if n odd, include extra factor of x
            result *= x
        return result

class PowerTests(unittest.TestCase):

    def test_power(self):
        self.assertEqual(9, power(3, 2))
        self.assertEqual(65536, power(2, 16))

if __name__ == '__main__':
    unittest.main()
