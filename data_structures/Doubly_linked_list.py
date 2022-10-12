class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.pre = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        node = self.head
        size = 0
        while node:
            size += 1
            node = node.next
        return size

    def add(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def append(self, data):
        node = Node(data)
        if self.tail is None:
            self.tail = node
            self.head = node
        else:
            node.pre = self.tail
            self.tail.next = node
            self.tail = node

    def print(self):
        node = self.head
        while node.next:
            print(node.data, end="<->")
            node = node.next
        print(node.data)

    def print_reverse(self):
        node = self.tail
        while node.pre:
            print(node.data, end="<->")
            node = node.pre
        print(node.data)
