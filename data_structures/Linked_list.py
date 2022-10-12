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
        if self.head.data == data:
            self.head = self.head.next
        node = self.head
        pre_node = node
        while node:
            if node.data == data:
                pre_node.next = node.next
                if not all:
                    return
            pre_node = node
            node = node.next

    def remove_head(self):
        if self.head is not None:
            self.head = self.head.next

    def remove_at(self, index):
        if index == 0:
            self.remove_head()
            return
        node = self.head
        pre_node = node
        cur_index = 0
        while node:
            if cur_index == index:
                pre_node.next = node.next
                return
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
                return
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
                return
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

    def _replace_head(self, new_node):
        if self.head is not None:
            new_node.next = self.head.next
            self.head = new_node

    def replace(self, index, data):
        new_node = Node(data)
        if index == 0:
            self._replace_head(new_node)
            return
        node = self.head
        pre_node = node
        cur_index = 0
        while node:
            if cur_index == index:
                pre_node.next = new_node
                new_node.next = node.next
                return
            cur_index += 1
            pre_node = node
            node = node.next

    def print(self):
        node = self.head
        if self.head is None:
            print("Empty")
        else:
            while node:
                if node.next is not None:
                    print(node.data, end="->")
                else:
                    print(node.data)
                node = node.next
