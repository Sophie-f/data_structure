# convert mathematical expression to tree and vice versa
from .ds_tree import*
from .ds_stack import Stack


def is_operator(s):
    if s in ['-', '+', '*', '/', '^', '~']:
        return True
    return False    


#################################################################
my_exp = '((a+b)*(c-d))'


# از مرتبه n^2
def infix_to_tree(exp, parent=None):
    if len(exp) == 1:
        return NodeTree(parent, exp[0])
    count = 0
    for k in range(1, len(exp)-1):
        elmnt = exp[k]
        if elmnt == '(':
            count += 1
        if elmnt == ')':
            count -= 1
        if count == 0:
            if is_operator(exp[k]):
                new_node = NodeTree(parent, exp[k])
                new_node.right = infix_to_tree(exp[k+1:len(exp)-1], new_node)
            else:
                new_node = NodeTree(parent, exp[k+1])
                new_node.left = infix_to_tree(exp[1:k+1], new_node)
                new_node.right = infix_to_tree(exp[k+2:len(exp)-1], new_node)    
            return new_node


print_inorder(infix_to_tree(my_exp))
print('\n')
# #####################################################################
# def inorder_to_tree_2(exp, parent = None): #از مرتبه n
#     if exp[0].isalnum():
#         return NodeTree(parent, exp[0])
#         if exp[0] == '(':
#             new_node = NodeTree(parent, None)
#             new_node.left = inorder_to_tree_2(exp[1:], new_node)
#             new_node.value = exp[2]
#             new_node.right =inorder_to_tree_2(exp[3:], new_node) 
#             if 
#             return new_node

#########################################################################
my_exp = 'ab+cd-*'


# it dose not work for unary operator, well
def postfix_to_tree(exp, parent=None):
    if exp == '':
        return None, None

    index = len(exp)-1
    if not is_operator(exp[index]):
        return NodeTree(parent, exp[index]), index
    new_node = NodeTree(parent, exp[index])
    result = postfix_to_tree(exp[:index], new_node)
    new_node.right = result[0]
    result = postfix_to_tree(exp[:result[1]], new_node)
    new_node.left = result[0]
    return new_node, result[1]


print_inorder(postfix_to_tree(my_exp)[0])    
print('\n')
#########################################################################


my_exp = '*+ab-cd'


# it dose not work for unary operator at all
def prefix_to_tree(exp, parent=None, count=0):
    if not is_operator(exp[count]):
        new = NodeTree(parent, exp[count])
        count += 1
        return new, count
    new_node = NodeTree(parent, exp[count])
    count += 1
    result = prefix_to_tree(exp, new_node, count)
    new_node.left = result[0]
    count = result[1]
    result = prefix_to_tree(exp, new_node, count)
    count = result[1]
    new_node.right = result[0]

    return new_node, count


print_inorder(prefix_to_tree(my_exp)[0])    
print('\n')

#########################################################################


my_exp = '((a+b)*(c-d))'


def infix_to_postfix(exp):
    post = []
    s = Stack(len(exp))
    for elm in exp:
        if elm.isalnum():
            post.append(elm)
        elif elm is '(':
            s.push(elm)
        elif elm is')':
            s.push(elm)
        # else:
        #
