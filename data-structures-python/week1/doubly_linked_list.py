class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        n = DNode(data)
        if not self.head:
            self.head = self.tail = n
            return
        n.prev = self.tail
        self.tail.next = n
        self.tail = n

    def prepend(self, data):
        n = DNode(data)
        if not self.head:
            self.head = self.tail = n
            return
        n.next = self.head
        self.head.prev = n
        self.head = n

    def remove(self, node):
        if node.prev: node.prev.next = node.next
        else: self.head = node.next
        if node.next: node.next.prev = node.prev
        else: self.tail = node.prev
        node.prev = node.next = None