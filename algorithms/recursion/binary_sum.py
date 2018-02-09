import unittest

def binary_sum(S, start, stop):
    """Return the sum of the numbers in implicit slice S[start:stop]."""
    if start >= stop:               # zero elemetns in slice
        return 0
    elif start == stop - 1:
        return S[start]             # one element in slice
    else:                           # two or more elements in slice
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)

class BinarySumTests(unittest.TestCase):

    def test_binary_sum(self):
        S = [4, 3, 6, 2, 8]
        self.assertEqual(23, binary_sum(S, 0, len(S)))

if __name__ == '__main__':
    unittest.main()
