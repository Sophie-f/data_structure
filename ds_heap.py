class MaxHeap:
    def __init__(self):
        self.heap = [0]

    def size(self):
        return len(self.heap)-1

    def bubble_up(self, i):
        while i > 1 and self.heap[i] > self.heap[i//2]:
            self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i = i//2

    def bubble_down(self, ind):
        while ind * 2 <= self.size():
            new_ind = ind
            if self.heap[2 * ind] > self.heap[ind]:
                new_ind = ind*2
            if 2 * ind + 1 <= self.size() and self.heap[2*ind + 1] > self.heap[new_ind]:
                new_ind = 2*ind + 1
            if new_ind == ind:
                break
            self.heap[ind], self.heap[new_ind] = self.heap[new_ind], self.heap[ind]
            ind = new_ind

    def insert(self, item):
        self.heap.append(item)
        self.bubble_up(self.size())

    def build_heap_with_bubble_down(self, my_list):
        self.heap.extend(my_list)
        for i in range(self.size(), 0, -1):
            self.bubble_down(i)

    def build_heap_with_bubble_up(self, my_list):
        self.heap.extend(my_list)
        for i in range(1, self.size()+1):
            self.bubble_up(i)

    def get_max(self):
        if self.size() == 0:
            raise Exception("heap is empty")
        return self.heap[1]

    def delete_max(self):
        if self.size() == 0:
            raise Exception("heap is empty")
        maximum = self.heap[1]
        self.heap[1] = self.heap[-1]
        self.heap.pop(-1)
        self.bubble_down(1)
        return maximum

    def clear(self):
        self.heap = [0]


heap = MaxHeap()
heap.build_heap_with_bubble_up([2, 4, 6, 4, 5, 3, 6])
print(heap.heap)
heap.clear()
heap.build_heap_with_bubble_down([2, 4, 6, 4, 5, 3, 6])
print(heap.heap)
print(heap.delete_max())
print(heap.heap)
heap.insert(9)
print(heap.get_max())
print(heap.heap)
print(heap.delete_max())
print(heap.delete_max())
print(heap.heap)
print(heap.size())