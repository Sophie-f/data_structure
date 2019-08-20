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


def search(node, value): 
    if node is None or node.value == value:
        return node
    elif value < node.value:    
        return search(node.left, value)
    else:    
        return search(node.right, value)  


def print_inorder(node):
    if node is None:
        return
    print_inorder(node.left)
    print(node.value)
    print_inorder(node.right)

    
def print_preorder(node):
    if node is None:
        return
    print(node.value)
    print_preorder(node.left)
    print_preorder(node.right)


def print_postorder(node):
    if node is None:
        return
    print_postorder(node.left)
    print_postorder(node.right)
    print(node.value)  


def min_node(node):  # find lowest child
    if node.left is None:
        return node
    return min_node(node.left)  


def max_node(node):  # find biggest child
    if node.right is None:
        return node 
    return max_node(node.right)  


def lca(current_root, x, y):  # finding lowest common ancestor
    if current_root.value > x.value and current_root.value > y.value:
        return lca(current_root.left, x, y)
    elif current_root.value < x.value and current_root.value < y.value:
        return lca(current_root.right, x, y)
    # elif current_root.value < x.value or current_root.value < y.value or current_root == x or current_root == y:
    #     return current_root
    # else:
    #     lca(current_root.left, x, y)
    else:
        return current_root
      

def replace(old_node, new_node):
    if old_node.parent: #oldNode is not root
        if old_node.parent.left == old_node:
            old_node.parent.left = new_node
        else:
            old_node.parent.right = new_node
    if new_node:
        new_node.parent = old_node.parent


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


root = NodeTree(None, 7)
insert(root, 2)
insert(root, 7)
insert(root, 4)
insert(root, 5)
insert(root, 6)
insert(root, 8)
insert(root, 5)
insert(root, 3)
insert(root, 9)
insert(root, 3)

print_preorder(root)
print(' ')
print(lca(root, search(root, 5), search(root, 6)).value)
