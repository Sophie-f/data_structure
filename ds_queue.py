class Queue:

    def __init__(self, max_size):
        self.max_size = max_size
        self.arry = [0]*max_size
        self.first = 0
        self.number = 0

    def enqueue(self, item):
        if self.number >= self.max_size:
            raise Exception("queue overflow")
        self.arry[(self.first+self.number) % self.max_size] = item
        self.number += 1

    def dequeue(self): 
        if self.number == 0:
            raise Exception("queue empty")
        item = self.arry[self.first]
        self.first += (1 + self.first) % self.max_size
        self.number -= 1
        return item

    def is_empty(self):
        return self.number == 0

    def size(self):
        return self.number

    def is_full(self):
        return self.number == self.max_size

    def front(self):
        if self.number == 0:
            raise Exception("queue empty")
        return self.arry[self.first]


# queue = Queue(5)
# print(queue.size())
# queue.enqueue('fresh')
# print(queue.size())
# queue.enqueue('mor')
# print(queue.size())
# print(queue.front())
# queue.dequeue()
# print(queue.size())
# print(queue.front())