'''
TASK OBJECTIVE:

Implement TREE_SORT algorithm in a language of your choice, but make sure that the
INORDER function is implemented iteratively.
'''

class BinTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def tree_insert(tree, item):
    if tree == None:
        tree = BinTreeNode(item)
    else:
        if (item < tree.value):
            if (tree.left == None):
                tree.left = BinTreeNode(item)
            else:
                tree_insert(tree.left, item)
        else:
            if (tree.right == None):
                tree.right = BinTreeNode(item)
            else:
                tree_insert(tree.right, item)
    return tree


def postorder(tree):
    if (tree.left != None):
        postorder(tree.left)
    if (tree.right != None):
        postorder(tree.right)
    print(tree.value)


def in_orderRec(tree):
    if (tree.left != None):
        in_order(tree.left)
    print(tree.value)
    if (tree.right != None):
        in_order(tree.right)

def in_orderIt(tree, A):
    buffer = []
    while True:

        #Check whether current node was buffered
        if buffer and tree == buffer[-1]:
            del buffer[-1]
            tree.left = None

        if tree.left == None:
            print(tree.value)
            if tree.right != None:
                tree = tree.right
            elif buffer:
                tree = buffer[-1]
            else:
                break
        else:
            if tree.right != None:
                buffer.append(tree)
            tree = tree.left


def TreeSort(A):
    t = tree_insert(None, A[0])
    for i in range(1, len(A)):
        tree_insert(t, A[i])
    in_orderIt(t, A)

if __name__ == '__main__':
    A = [6, 10, 234, 534, 5, 2, 1, 0, 24, 10, 3, 4, 11]
    TreeSort(A)