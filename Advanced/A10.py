#I deleted all links to node we want to delete. Do I have to delete the node itself somehow?

class Node(object):
    def __init__(self, value, next):
        self.value = value
        self.next = next


class List(object):
    def __init__(self, new):
        self.head = Node(new, None)
        self.head.next = self.head

    def insert(self, new):
        self.head.next = Node(new, self.head.next)

    def display(self, n):
        values = []
        old = self.head
        for i in range(n):
            values.append(str(old.value))
            old = old.next
        print("List: ", ",".join(values))

    def delete(self, n):

        if n == self.head.value:
            self.head = self.head.next

        current = self.head.next
        found = False
        size = 0
        while not found:
            if current.value == self.head.value:
                found = True
            else:
                current = current.next
            size += 1

        current = self.head
        found = False
        while current.value != n:
                current = current.next
        for i in range(size-1):
            current = current.next
        current.next = current.next.next
        for i in range(size+1):
            self.head = self.head.next

    def play(self, n, Start):
        current = self.head
        left = n

        while current.value != Start:
            current = current.next

        while left > 1:
            print('Counting: ', current.value)
            for i in range(n):
                current = current.next
            print('Killing: ', current.value)
            l.delete(current.value)
            current = current.next
            print('WIll count: ', current.value)
            l.display(4)
            left -= 1
            print()
        return current.value

if __name__ == '__main__':

    n = 4
    Names = ['Diana', 'Michael', 'David','Mary']
    Start = 'Diana'

    # I assume next counting person is the one after killed one
    for i in reversed(range(n)):
        if i==n-1:
            l = List(Names[0])
        else:
            l.insert(Names[i+1])
    print('WINNER: ', l.play(n, Start))
