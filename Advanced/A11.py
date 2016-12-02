# include <iostream>

class BinTreeNode(object):
    def __init__(self, word, frequency):
        self.word = word
        self.frequency = frequency
        self.left = None
        self.right = None


def tree_insert(tree, word, frequency):
    if tree == None:
        tree = BinTreeNode(word, frequency)
    else:
        if (word < tree.word):
            if (tree.left == None):
                tree.left = BinTreeNode(word, frequency)
            else:
                tree_insert(tree.left, word, frequency)
        else:
            if (tree.right == None):
                tree.right = BinTreeNode(word, frequency)
            else:
                tree_insert(tree.right, word, frequency)
    return tree

def preorder(tree):
    print(tree.word, tree.frequency)
    if (tree.left != None):
        preorder(tree.left)
    if (tree.right != None):
        preorder(tree.right)

def findWord(tree, word):
    print('Looking for word:', word)
    r = tree
    while r != None:
        print()
        print('Current word:', r.word)
        print('Frequency:', r.frequency)
        if r.word == word:
            return 'YES. WORD WAS FOUND!'
        elif r.word > word:
            print('Looking earlier in alphabet (left child)')
            r = r.left
        else:
            print('Looking further in alphabet (right child)')
            r = r.right
    return 'NO. WORD WAS NOT FOUND :('

if __name__ == '__main__':
    f = open('paragraph.txt', 'r')
    text = f.read()
    text = text.replace('.','')
    text = text.replace(',', '')
    t = None
    frequencies = {}
    for i in text.split():
        if i not in frequencies:
            frequencies[i] = 1
        else:
            frequencies[i] += 1
    for key, value in frequencies.items():
        if t == None:
            t = tree_insert(None, key, value)
        else:
            tree_insert(t, key, value)
    preorder(t)
    print()
    print(findWord(t, 'today'))