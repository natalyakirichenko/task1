import unittest

from queue import Queue


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.test_queue = Queue()

    def testEnqueue(self):
        self.assertEqual(self.test_queue.size(), 0)
        # assertTrue
        # assertFalse
        # Ctrl + Shift + F10 запускает текущий файл

    def testDequeue(self):
        self.assertTrue(self.test_queue.dequeue() is None)

    def testsize (self):
        return self.qsize

    def testclear (self):
        if self.qsize == 0:
            return None

        else:
            self.first = self.first.next
            self.qsize = self.qsize - 1
            return self.qsize


    def testfront(self):
        print(self.first)
        return self.first

    def testback(self):
        print(self.next)
        return self.next



