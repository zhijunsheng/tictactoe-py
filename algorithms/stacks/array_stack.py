class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self):
        """Create an empty stack."""
        self._data = []                 # nonpublic list instance

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)
