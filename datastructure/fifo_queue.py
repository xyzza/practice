class QueueNaive:
    """
    Naive implementation.
    """

    _queue = None

    def __init__(self):
        self._queue = []

    def add(self, item):
        """O(1)"""
        self._queue.append(item)

    def pop(self):
        """O(n) - that's bad"""
        return self._queue.pop(0)


class Queue:

    _tail = None
    _head = None

    def add(self, item):
        # O(1)
        # Adds new element.
        # Each previous element has a link to a new added
        # <- <- <-
        item = {"val": item, "tail": None}
        if self._tail is not None:
            # if it is not first addition -
            # establish a link from previous to a new one
            self._tail["tail"] = item

        if self._head is None:
            # save a link to a head of list
            self._head = item
        self._tail = item

    def pop(self):
        # O(1)
        val = self._head["val"]
        self._head = self._head["tail"]
        return val
