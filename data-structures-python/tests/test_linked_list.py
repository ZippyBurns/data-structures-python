from week1.linked_list import LinkedList

def test_append_find_delete_reverse():
    ll = LinkedList()
    for x in [1,2,3,4]:
        ll.append(x)
    assert ll.find(3)
    assert not ll.find(99)
    assert ll.delete(1)   # delete head
    assert ll.delete(3)   # delete middle
    assert not ll.delete(42)
    # remaining: 2 -> 4
    ll.reverse()
    # after reverse: 4 -> 2
    vals = []
    cur = ll.head
    while cur:
        vals.append(cur.data)
        cur = cur.next
    assert vals == [4,2]