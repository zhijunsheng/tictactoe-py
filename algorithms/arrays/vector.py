import unittest

class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        self._coords = [0] * d

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):             # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))              # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other            # rely on existing __eq__ definition

    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1: -1] + '>' # adapt list representation

class TestVector(unittest.TestCase):

    def test_vector_add(self):
        v1 = Vector(5)
        v1[0] = 7
        v2 = Vector(5)
        v2[0] = 2
        v2[4] = 3
        v3 = Vector(5)
        v3[0] = 9
        v3[4] = 3
        self.assertEqual(v3, v1 + v2)

    def test_vector_raise(self):
        v1 = Vector(5)
        v2 = Vector(4)
        self.assertRaises(ValueError, Vector.__add__, v1, v2)

if __name__ == '__main__':
    unittest.main()
