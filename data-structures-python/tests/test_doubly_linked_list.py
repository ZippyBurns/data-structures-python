from week1.doubly_linked_list import DoublyLinkedList

def test_dll_append_prepend_remove():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.prepend(0)
    # list: 0 <-> 1 <-> 2
    # remove middle
    node = dll.head.next  # node with 1
    dll.remove(node)
    # expect: 0 <-> 2
    assert dll.head.data == 0
    assert dll.tail.data == 2
    assert dll.head.next == dll.tail
    assert dll.tail.prev == dll.head