import heapq


class EventQueue:
    def __init__(self):
        # Internal heap storage
        self._heap = []
        # Sequence counter to break timestamp ties
        self._seq = 0

    def push(self, event):
        """
        Add an event to the queue.
        """
        # Push a tuple so heapq knows how to order events
        heapq.heappush(
            self._heap,
            (event.timestamp, self._seq, event)
        )
        self._seq += 1

    def pop(self):
        """
        Remove and return the earliest event.
        """
        _, _, event = heapq.heappop(self._heap)
        return event

    def peek(self):
        """
        Return the earliest event without removing it.
        """
        _, _, event = self._heap[0]
        return event

    def is_empty(self):
        """
        Check if the queue has no events.
        """
        return len(self._heap) == 0
