class Element:

    def __init__ (self, value):
        self.value = value
        self.next = None


class Queue:



    def __init__(self):
        self.first = None
        self.last = None
        self.qsize = 0

    def enqueue(self, value):

        newelement = Element(value)

        if self.qsize == 0:
            self.first = self.last = newelement

        else:
            self.last.next = newelement
            self.last = newelement

        self.qsize = self.qsize + 1

    def dequeue(self):

        if self.qsize == 0:
            return None

        else:
            tempelement = self.first
            self.first = self.first.next
            self.qsize = self.qsize - 1
            return tempelement.value

    def size(self):
        return self.qsize

    def clear(self):
       if self.qsize == 0:
           return None

       else:
           self.first = self.first.next
           self.qsize = self.qsize - 1


    def front(self):
        print(self.first)
        return self.first

    def back(self):
        print(self.next)
        return self.next

