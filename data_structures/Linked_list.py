class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        node = self.head
        size = 0
        while node:
            size += 1
            node = node.next
        return size

    def add(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node

    def find(self, data):
        cur = self.head
        index = 0
        while cur:
            if cur.data == data:
                return index
            cur = cur.next
            index += 1
        return None

    def remove(self, data, all=False):
        node = self.head
        pre_node = node
        while node:
            if node.data == data:
                pre_node.next = node.next
                if not all:
                    break
            pre_node = node
            node = node.next

    def remove_at(self, index):
        node = self.head
        pre_node = node
        cur_index = 0
        while node:
            if cur_index == index:
                pre_node.next = node.next
                break
            pre_node = node
            node = node.next
            cur_index += 1

    def insert_after(self, data, index):
        ins_node = Node(data)
        node = self.head
        cur_index = 0
        while node:
            if cur_index == index:
                ins_node.next = node.next
                node.next = ins_node
                break
            node = node.next
            cur_index += 1

    def insert_before(self, data, index):
        ins_node = Node(data)
        node = self.head
        pre_node = node
        cur_index = 0
        while node:
            if cur_index == index:
                ins_node.next = node
                pre_node.next = ins_node
                break
            pre_node = node
            node = node.next
            cur_index += 1

    def reverse(self):
        node = self.head
        link = LinkedList()
        while node:
            link.add(node.data)
            node = node.next
        self.head = link.head

    def print(self):
        cur = self.head
        if self.head is None:
            print("Empty")
        else:
            while cur:
                if cur.next is not None:
                    print(cur.data, end="->")
                else:
                    print(cur.data)
                cur = cur.next
