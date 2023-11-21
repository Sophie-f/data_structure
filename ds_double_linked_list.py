class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoubleLinkList:
    def __init__(self):
        self.head = Node(None)  # the node before first node that has first data
        self.head.prev = self.head  # the pervious element of a node should be a node
        self.head.next = self.head  # the next element of a node should be a node
        self.n = 0

    def insert_after(self, last_node, new_data):   # last_node: the last node before inserting new_data that is not None
        current_node = Node(new_data)
        self.n += 1
        current_node.prev = last_node     
        current_node.next = last_node.next  # None #the next element of a node should be a node
        last_node.next = current_node 
        current_node.next.prev = current_node

    def get(self, index):
        if index >= self.size():
            raise Exception("out of list")
        current_node = self.head.next  # node that has first data
        for i in range(index):
            current_node = current_node.head.next
        return current_node

    def find(self, value):
        current_node = self.head.next  # node that has first data
        for i in range(self.size()):
            if current_node.data == value:
                return current_node
            current_node = current_node.next
        return None

    def delete(self, x):  # x: node that will be deleted
        self.n -= 1
        x.prev.next = x.next
        x.next.prev = x.prev
        return x

    def size(self):
        return self.n

    def is_empty(self):
        return self.n == 0   


my_list = DoubleLinkList() # head
print(my_list.size())
my_list.insert_after(my_list.head,"Fresht") # head <-> Fresht
print(my_list.size())
my_list.insert_after(my_list.get(0),"Mortz") # head <-> Fresht <-> Mortz
print(my_list.size())
my_list.insert_after(my_list.find("Mortz").prev,"Fati") # head <-> Fresht <-> Fati <-> Mortz 
print(my_list.get(0).data)
print(my_list.get(1).data)
print(my_list.get(2).data)

print(my_list.size())
my_list.delete(my_list.find("Fati")) # head <-> Feresht <-> Mortz
print(my_list.size())
