#I deleted all links to node we want to delete. Do I have to delete the node itself somehow?

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class List(object):
    def __init__(self):
        self.head = None # first element in the list
        self.tail = None # last element

    def insert(self, old, new): # n = previous node/location where to place node    x = new node
        # Not actually perfect: how do we prepend to an existing list?
        # if this is NOT first element
        if old != None:
            new.next = old.next #Attach next-link to new node
            old.next = new #Attach next-link to old node
            new.prev = old #Attach prev-link to new node
            if new.next != None: #If the old node was the last one
                new.next.prev = new # NO FUCKING IDEA WHAT THIS MEANS!!!

        # If this is first element
        if self.head == None:
            self.head = self.tail = new # node becomes head and tail
            new.prev = new.next = None # there is no prev/next nodes
        elif self.tail == old: #If the new node was added to tail, the tail is now new node
            self.tail = new

    def display(self):
        values = []
        old = self.head
        while old != None:
            values.append(str(old.value))
            old = old.next
        print("List: ", ",".join(values))

    def delete(self, n):

        # Locating the node
        node = self.head
        while node.value != n:
            node = node.next
            if node == self.tail:
                print("There is no such node")
                break

        # Deleting all links to node
        if node != self.tail and node != self.head:
            node.prev.next=node.next
            node.next.prev=node.prev
        elif node == self.tail: # Node is the last one
            self.tail = node.prev
            node.prev.next = None
        elif node == self.head: # Node is the first one
            self.head = node.next
            node.next.prev = None
        #Question left - whether I should delete the node itself, if all the links are deleted

if __name__ == '__main__':
    l = List()
    l.insert(None, Node(4))
    l.insert(l.head, Node(6))
    l.insert(l.head, Node(8))
    l.insert(l.tail, Node(5))
    l.insert(l.head, Node(9))
    l.insert(l.tail, Node(1))
    l.delete(4)

    l.display()