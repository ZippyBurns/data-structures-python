class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        n = Node(data)
        n.next = self.head
        self.head = n

    def append(self, data):
        n = Node(data)
        if not self.head:
            self.head = n
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = n

    def find(self, value):
        cur = self.head
        while cur:
            if cur.data == value:
                return True
            cur = cur.next
        return False

    def delete(self, value):
        cur = self.head
        prev = None
        while cur:
            if cur.data == value:
                if prev: prev.next = cur.next
                else: self.head = cur.next
                return True
            prev, cur = cur, cur.next
        return False

    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev