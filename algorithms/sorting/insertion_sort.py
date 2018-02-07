import unittest

def insertion_sort(A):
    """Sort list of comparable elements into nondescreasing order."""
    for k in range(1, len(A)):          # from 1 to n - 1
        cur = A[k]                      # current element to be inserted
        j = k                           # find correct index j for current
        while j > 0 and A[j - 1] > cur: # element A[j - 1] must be after current
            A[j] = A[j - 1]
            j -= 1
        A[j] = cur                      # cur is now in the right place

class TestInsertionSort(unittest.TestCase):

    def test_insertion_sort(self):
        orig = [3, 7, 5]
        insertion_sort(orig)
        self.assertEqual([3, 5, 7], orig)

        strings = ['d', 'a']
        insertion_sort(strings)
        self.assertEqual(['a', 'd'], strings)

if __name__ == '__main__':
    unittest.main()
