import unittest

def binary_search(data, target, low, high):
    """Return True if target is found in indicated potion of a Python list.

    The searvh only considers the portion from data[low] to data[high] inclusive.
    """
    if low > high:
        return False                # interval is empty; no match
    else:
        mid = (low + high) // 2
        if target == data[mid]:     # found a match
            return True
        elif target < data[mid]:
            # recur on the portion left of the middle
            return binary_search(data, target, low, mid - 1)
        else:
            # recur on the portion right of the middle
            return binary_search(data, target, mid + 1, high)

class TestBinarySearch(unittest.TestCase):

    def test_binary_search(self):
        sorted_ints = [1, 2, 3]
        self.assertTrue(binary_search(sorted_ints, 3, 0, 2))
        self.assertFalse(binary_search(sorted_ints, 0, 0, 2))

if __name__ == '__main__':
    unittest.main()
