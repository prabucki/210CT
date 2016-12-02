'''
TASK OBJECTIVE:

Using the model of a circular single-linked list, implement the following scenario:
N children stand in a circle; one of the children starts counting the others clockwise. Every
Nth child leaves the game. The winner is the one who remains.
Notes: Read the number of children, the childrens' names and the one starting to count
from the standard input. Input: 4; Diana, Michael, David, Mary; Start: Diana; Winner:
Michael.
'''

class Node(object):
    def __init__(self, value, next):
        self.value = value
        self.next = next


class List(object):
    def __init__(self, new):
        self.head = Node(new, None)
        self.head.next = self.head

    def insert(self, new):
        ''' Insert new element after the head of list'''
        self.head.next = Node(new, self.head.next)

    def display(self, n):
        ''' Displays next n elements in circle'''

        values = []
        old = self.head
        for i in range(n):
            values.append(str(old.value))
            old = old.next
        print("List: ", ",".join(values))

    def delete(self, n):
        ''' Deletes element from circular list'''


        if n == self.head.value:
            self.head = self.head.next

        current = self.head.next
        found = False
        size = 0

        # Analyses linked list to determine its size
        while not found:
            if current.value == self.head.value:
                found = True
            else:
                current = current.next
            size += 1
        current = self.head

        # Searches linked list for node to delete
        while current.value != n:
                current = current.next

        # Changes link of every node to skip deleted one
        for i in range(size-1):
            current = current.next
        current.next = current.next.next
        for i in range(size+1):
            self.head = self.head.next

    def play(self, n, Start):
        '''Simulates the game of children counting each other.
        Requires list of children, name of child that counts first and returns the winner'''
        current = self.head
        left = n

        while current.value != Start:
            current = current.next

        while left > 1: # while there is more than one child in game
            print('--NEW ROUND--')
            print('Counting: ', current.value)

            for i in range(n): # count n next children
                current = current.next
            print('Killing: ', current.value)
            l.delete(current.value) # delete kid who lost from the list
            current = current.next # pick next kid to count
            print('WIll count next: ', current.value)
            l.display(n) # Shows next n names on list
            left -= 1
            print()
        return current.value

if __name__ == '__main__':

    # Variables
    n = 4
    Names = ['Diana', 'Michael', 'David','Mary']
    Start = 'Diana'

    # Note: I assume next counting person is the one after killed one (wasn't specified in the task)
    for i in reversed(range(n)): # Because of the circular list head pointing to end, names are entered in reverse
        if i == n - 1:  # If this is the first name to add
            l = List(Names[0])
        else:
            l.insert(Names[i+1])

    print()
    print('WINNER: ', l.play(n, Start))
