import unittest
import threading
import time
from producer_consumer import BoundedQueue, Producer, Consumer


# some basic queue tests
class TestBoundedQueueBasics(unittest.TestCase):

    def test_put_and_get_basic(self):
        queue = BoundedQueue(max_size=2)
        queue.put(10)
        queue.put(20)
        self.assertEqual(queue.get(), 10)
        self.assertEqual(queue.get(), 20)

    def test_queue_blocks_when_full(self):
        queue = BoundedQueue(max_size=1)
        result = []

        def producer_job():
            queue.put("A")
            queue.put("B")      # this should wait
            result.append("done")

        def consumer_job():
            time.sleep(0.15)
            self.assertEqual(queue.get(), "A")
            time.sleep(0.15)
            self.assertEqual(queue.get(), "B")

        t1 = threading.Thread(target=producer_job)
        t2 = threading.Thread(target=consumer_job)
        t1.start(); t2.start()
        t1.join(); t2.join()

        self.assertEqual(result, ["done"])

    def test_queue_blocks_when_empty(self):
        queue = BoundedQueue(max_size=2)
        result = []

        def consumer_job():
            result.append(queue.get())   # waits here

        def producer_job():
            time.sleep(0.15)
            queue.put("X")

        t1 = threading.Thread(target=consumer_job)
        t2 = threading.Thread(target=producer_job)
        t1.start(); t2.start()
        t1.join(); t2.join()

        self.assertEqual(result, ["X"])


# producer–consumer thread tests
class TestProducerConsumer(unittest.TestCase):

    def test_single_producer_consumer(self):
        source = list(range(1, 11))
        dest = []
        queue = BoundedQueue(max_size=3)
        sentinel = object()

        p = Producer(source, queue)
        c = Consumer(queue, dest, sentinel)

        p.start(); c.start()
        p.join()
        queue.put(sentinel)
        c.join()

        self.assertEqual(source, dest)

    def test_sentinel_stops_consumer(self):
        source = [1, 2, 3]
        dest = []
        queue = BoundedQueue(max_size=2)
        sentinel = "STOP"

        p = Producer(source, queue)
        c = Consumer(queue, dest, sentinel)

        p.start(); c.start()
        p.join()
        queue.put(sentinel)
        c.join()

        self.assertEqual(dest, source)

    def test_multiple_producers(self):
        queue = BoundedQueue(max_size=5)
        sentinel = None

        s1 = [1, 2, 3]
        s2 = [4, 5, 6]
        dest = []

        p1 = Producer(s1, queue)
        p2 = Producer(s2, queue)
        c = Consumer(queue, dest, sentinel)

        p1.start(); p2.start(); c.start()
        p1.join(); p2.join()
        queue.put(sentinel)
        c.join()

        self.assertCountEqual(dest, s1 + s2)

    def test_stress_100_items(self):
        source = list(range(100))
        dest = []
        queue = BoundedQueue(max_size=10)
        sentinel = object()

        p = Producer(source, queue)
        c = Consumer(queue, dest, sentinel)

        p.start(); c.start()
        p.join()
        queue.put(sentinel)
        c.join()

        self.assertEqual(source, dest)


# verbose demo to show the behaviour clearly
class VerboseProducer(threading.Thread):
    def __init__(self, source, queue, sentinel, delay=0.05):
        super().__init__()
        self.source = source
        self.queue = queue
        self.sentinel = sentinel
        self.delay = delay

    def run(self):
        print("Producer: Starting...")
        for item in self.source:
            print(f"Producer: putting {item} (queue size: {len(self.queue._items)})")
            self.queue.put(item)
            time.sleep(self.delay)
        print("Producer: Done")
        self.queue.put(self.sentinel)


class VerboseConsumer(threading.Thread):
    def __init__(self, queue, dest, sentinel, delay=0.1):
        super().__init__()
        self.queue = queue
        self.dest = dest
        self.sentinel = sentinel
        self.delay = delay

    def run(self):
        print("Consumer: Starting...")
        while True:
            print(f"Consumer: waiting... (queue size: {len(self.queue._items)})")
            item = self.queue.get()

            if item == self.sentinel:
                print("Consumer: received sentinel, stopping")
                print("Consumer: Done")
                break

            self.dest.append(item)
            print(f"Consumer: got {item} → dest={self.dest}")
            time.sleep(self.delay)


class TestVerboseDemo(unittest.TestCase):
    def test_verbose_demo(self):
        source = [1, 2, 3, 4, 5]
        dest = []
        queue = BoundedQueue(max_size=3)
        sentinel = None

        vp = VerboseProducer(source, queue, sentinel, delay=0.03)
        vc = VerboseConsumer(queue, dest, sentinel, delay=0.05)

        print("\n=== PRODUCER–CONSUMER DEMO START ===\n")

        vp.start()
        vc.start()
        vp.join()
        vc.join()

        print("\n=== PRODUCER–CONSUMER DEMO END ===\n")

        self.assertEqual(dest, source)


if __name__ == "__main__":
    unittest.main()
