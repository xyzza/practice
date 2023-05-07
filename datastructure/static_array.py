class StaticArray:
    def __init__(self, sequence):
        self._data = [el for el in sequence]

    def __iter__(self):
        return self._data

    def get_at(self, i):
        return self._data[i]

    def set_at(self, i, value):
        self._data[i] = value
