import unittest

def linear_sum(S, n):
    """Return the sum of the first n numbers of sequence S."""
    if n == 0:
        return 0
    else:
        return linear_sum(S, n - 1) + S[n - 1]

class TestLinearSum(unittest.TestCase):

    def test_linear_sum(self):
        S = [4, 3, 6, 2, 8]
        self.assertEqual(23, linear_sum(S, 5))

if __name__ == '__main__':
    unittest.main()
