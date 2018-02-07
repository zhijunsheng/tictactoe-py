import unittest


class TestIterator(unittest.TestCase):

    def test_iterator(self):
        data = [1, 2, 4, 8]
        i = iter(data)
        self.assertEqual(1, next(i))
        self.assertEqual(2, next(i))
        self.assertEqual(4, next(i))
        self.assertEqual(8, next(i))
        self.assertRaises(StopIteration, next, i)

    def test_iterable_range(self):
        l = list(range(10))
        self.assertEqual(10, len(l))

    def factor(self, n):
        for k in range(1, n + 1):
            if n % k == 0:
                yield k

    def test_generator(self):
        i = iter(self.factor(100))
        self.assertEqual(1, next(i))
        self.assertEqual(2, next(i))
        self.assertEqual(4, next(i))
        self.assertEqual(5, next(i))
        self.assertEqual(10, next(i))
        self.assertEqual(20, next(i))
        self.assertEqual(25, next(i))
        self.assertEqual(50, next(i))
        self.assertEqual(100, next(i))
        self.assertRaises(StopIteration, next, i)

    def fibonacci(self):
        a = 0
        b = 1
        while True:             # keep going...
            yield a             # report value, a, during this pass
            future = a + b
            a = b               # this will be next value reported
            b = future          # and subsequently this

    def test_fibonacci(self):
        i = iter(self.fibonacci())
        self.assertEqual(0, next(i))
        self.assertEqual(1, next(i))
        self.assertEqual(1, next(i))
        self.assertEqual(2, next(i))
        self.assertEqual(3, next(i))
        self.assertEqual(5, next(i))
        self.assertEqual(8, next(i))
        self.assertEqual(13, next(i))
        self.assertEqual(21, next(i))

if __name__ == '__main__':
    unittest.main()
