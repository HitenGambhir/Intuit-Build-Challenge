import threading
from typing import List, Any


class BoundedQueue:
    """
    Thread-safe bounded queue.
    Blocks producers when full and consumers when empty.
    """

    def __init__(self, max_size: int):
        self.max_size = max_size
        self._items: List[Any] = []

        # Lock + conditions control access and manage waiting threads
        self._lock = threading.Lock()
        self._not_empty = threading.Condition(self._lock)
        self._not_full = threading.Condition(self._lock)

    def put(self, item: Any) -> None:
        """Wait if queue is full, otherwise insert item."""
        with self._not_full:
            while len(self._items) >= self.max_size:
                self._not_full.wait()     # producer waits

            self._items.append(item)
            self._not_empty.notify()      # signal consumer

    def get(self) -> Any:
        """Wait if queue is empty, otherwise remove item."""
        with self._not_empty:
            while len(self._items) == 0:
                self._not_empty.wait()    # consumer waits

            item = self._items.pop(0)
            self._not_full.notify()       # signal producer
            return item


class Producer(threading.Thread):
    """
    Reads items from a source list and pushes them into the queue.
    Sentinel is added externally after all producers finish.
    """

    def __init__(self, source: List[Any], queue: BoundedQueue, delay: float = 0.0):
        super().__init__()
        self.source = source
        self.queue = queue
        self.delay = delay

    def run(self):
        for item in self.source:
            self.queue.put(item)
            if self.delay > 0:
                import time
                time.sleep(self.delay)


class Consumer(threading.Thread):
    """
    Reads items from the queue and stores them in destination list.
    Stops when a sentinel value is received.
    """

    def __init__(self, queue: BoundedQueue, destination: List[Any], sentinel: Any, delay: float = 0.0):
        super().__init__()
        self.queue = queue
        self.destination = destination
        self.sentinel = sentinel
        self.delay = delay

    def run(self):
        import time
        while True:
            item = self.queue.get()

            if item == self.sentinel:
                break

            self.destination.append(item)

            if self.delay > 0:
                time.sleep(self.delay)
