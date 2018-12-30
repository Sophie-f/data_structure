class Node:
    def __init__(self):
        self.count = 0
        self.edge = []


class Edge:
    def __init__(self, label, start, end):
        self.start = start
        self.end = end
        self.label = label

        
def insert(node, string, idx=0):
    if len(string) == idx:
        node.count += 1
        return 
    found = False    
    for edge in node.edge:
        if edge.label == string[idx]:
            found = True
            insert(edge.end, string, idx + 1)
            break
    if not found:
        new_node = Node()            
        new_edge = Edge(string[idx], node, new_node)
        node.edge.append(new_edge) 
        insert(new_node, string, idx+1)


def search(node, string, idx=0):
    if len(string) == idx:
        return node.count
    for edge in node.edge:
        if edge.label == string[idx]:
            return search(edge.end, string, idx + 1)
    return 0  


def delete(node, string, idx=0):
    if len(string) == idx:
        if node.count == 0:
            raise Exception("item not found")
        node.count -= 1
        return
    for edge in node.edge:
        if edge.label == string[idx]:
            return delete(edge.end, string, idx + 1)
    raise Exception("item not found")


root = Node()
insert(root, 'hi')
insert(root, 'hi')
insert(root, 'hi')
insert(root, 'hi')
print(search(root, 'hi'))
delete(root, 'hi')
print(search(root, 'hi'))
