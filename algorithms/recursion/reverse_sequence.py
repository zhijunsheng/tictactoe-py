import unittest

def reverse(S, start, stop):
    """Reverse elements in implicit slice S[start:stop]."""
    if start < stop - 1:                                # if at least 2 elements:
        S[start], S[stop - 1] = S[stop - 1], S[start]    # swap first and last
        reverse(S, start + 1, stop - 1)                 # recur on rest

class TestReverseSequence(unittest.TestCase):

    def test_reverse(self):
        S = [4, 3, 6, 2, 8]
        reverse(S, 0, 5)
        self.assertEqual([8, 2, 6, 3, 4], S)

if __name__ == '__main__':
    unittest.main()
