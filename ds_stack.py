class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.num = 0
        self.S = self.max_size*[0]

    def push(self, item):
        if self.num >= self.max_size:
            raise Exception("stack overflow")
        self.S[self.num] = item
        self.num += 1

    def pop(self):
        if self.num <= 0:
            raise Exception("stack empty")
        self.num -= 1
        return self.S[self.num]

    def is_empty(self):
        return self.num == 0

    def size(self):
        return self.num

    def top(self):
        if self.num == 0:
            raise Exception("stack empty")
        return self.S[self.num-1]
