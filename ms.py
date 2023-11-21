l = [12,5,7, 7,3]
k=3
class NodeTree:
    def __init__(self, parent, value):
        self.parent = parent
        self.value = value
        self.left = None
        self.right = None


def insert(parent, value):
    if value <= parent.value:
        if parent.left is None:
            parent.left = NodeTree(parent, value)
            return
        insert(parent.left, value)  
    else:
        if parent.right is None:
            parent.right = NodeTree(parent, value)
            return
        insert(parent.right, value) 



def replace(old_node, new_node):
    if old_node.parent: #oldNode is not root
        if old_node.parent.left == old_node:
            old_node.parent.left = new_node
        else:
            old_node.parent.right = new_node
    if new_node:
        new_node.parent = old_node.parent

def max_node(node):  # find biggest child
    if node.right is None:
        return node 
    return max_node(node.right)  


def delete(node):
    if node is None:
        return
    if node.right is None:
        replace(node, node.left)
    elif node.left is None:
        replace(node, node.right)   
    else:
        temp = node.left 
        while temp.right is not None:
            temp = temp.right
        node.value = temp.value
        delete(temp)


root = NodeTree(None, 0)
for i in l:
    insert(root,i)


for i in range(k):
    m= max_node(root)
    insert(root,(m.value+1)//2)
    delete(m)

    if m is root: 
        m.value=0

def count(node):
    if node is None:
        return 0
    return node.value + count(node.left) + count(node.right)

def print_preorder(node):
    if node is None:
        return
    print(node.value)
    print_preorder(node.left)
    print_preorder(node.right)

print(count(root))
print_preorder(root)