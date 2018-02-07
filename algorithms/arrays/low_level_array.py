import unittest
from array import array
import sys

class TestArray(unittest.TestCase):

    def test_compact_array(self):
        primes = array('i', [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(7, primes[3])

    def test_amortization(self):
        data = []
        for k in range(27):
            b = sys.getsizeof(data)
            if k == 0:
                self.assertEqual(72, b)
            elif k < 5:
                self.assertEqual(72 + 32, b)
            elif k < 9:
                self.assertEqual(72 + 32 + 32, b)
            elif k < 17:
                self.assertEqual(72 + 32 + 32 + 64, b)
            elif k < 26:
                self.assertEqual(72 + 32 + 32 + 64 + 72, b)
            elif k < 27:
                self.assertEqual(72 + 32 + 32 + 64 + 72 + 80, b)
            data.append(None)


if __name__ == '__main__':
    unittest.main()
