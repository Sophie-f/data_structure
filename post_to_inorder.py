class NodeTree:
    def __init__(self, parent, value):
        self.parent = parent
        self.value = value
        self.left = None
        self.right = None


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


# نمایش پری و پست اردر به ما داده شده 
# و باید نمایش این اردر را در خروجی چاپ کنیم
#  با این فرض که ورودی ها کلمه اند و اگر یک فرزند وجود داشت ان را چپ در نظر بگیریم

preorder_list = ['m', 'n', 'h', 'c', 'r', 's', 'k', 'w', 't', 'g', 'd', 'x', 'i',
                 'y', 'a', 'j', 'p', 'o', 'e', 'z', 'v', 'b', 'u', 'l', 'q', 'f']

postorder_list = ['c', 'w', 't', 'k', 's', 'g', 'r', 'h', ' d', 'n', 'a', 'o', 'e',
                  'p', 'j', 'y', 'z', 'i', 'b', 'q', 'l', 'f', 'u', 'v', 'x', 'm']

root = NodeTree(None, preorder_list[0])


def make_tree(pre, post, parent):
    if len(post) == 1:
        return
    start = pre[1]
    end = post[len(post)-2]
    left_node = NodeTree(parent, start)
    parent.left = left_node 
    if start == end:
        parent.right = None
        make_tree(pre[1:], post[:post.index(start)+1], left_node)
    else:
        right_node = NodeTree(parent, end)
        parent.right = right_node
        make_tree(pre[1:pre.index(end)], post[:post.index(start)+1], left_node)
        make_tree(pre[pre.index(end):], post[post.index(start)+1:len(post)-1], right_node) 


make_tree(preorder_list, postorder_list, root)
print_inorder(root) 


# نمایش پری و پست اردر به ما داده شده 
# و باید نمایش این اردر را در خروجی چاپ کنیم
#  با این فرض که ورودی ها عدد هستند

preorder_list = [6, 2, 4, 3, 3, 5, 5, 6, 7, 8, 9]
postorder_list = [3, 3, 5, 6, 5, 4, 2, 9, 8, 7, 6]
root = NodeTree(None, preorder_list[0])


def make_tree_num(pre, post, parent):
    print(pre, post)
    if len(post) == 1:
        return
    start = pre[1]
    end = post[len(post)-2]
    if start == end:
        if start <= parent.value:
            left_node = NodeTree(parent, start)
            parent.left = left_node 
            make_tree_num(pre[1:], post[:len(post)-1], left_node)
            parent.right = None 
        else:
            right_node = NodeTree(parent, end)
            parent.right = right_node
            make_tree_num(pre[1:], post[:len(post)-1], right_node)
            parent.left = None
    else:
        right_node = NodeTree(parent, end)
        parent.right = right_node
        left_node = NodeTree(parent, start)
        parent.left = left_node
        make_tree_num(pre[1:pre.index(end)], post[:post.index(start)+1], left_node)
        make_tree_num(pre[pre.index(end):], post[post.index(start)+1:len(post)-1], right_node) 


make_tree_num(preorder_list, postorder_list, root)
print_inorder(root)
