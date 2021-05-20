from dataclasses import dataclass, field

@dataclass(order=True)
class LinkedList:
    value: int
    next_node: str = field(compare=False, default=None, repr=False)
    prev_node: str = field(compare=False, default=None, repr=False)

if __name__ == '__main__':
    parent_node = LinkedList(-1)
    cur_node = parent_node
    for i in range(20):
        cur_node.next_node = LinkedList(i)
        cur_node = cur_node.next_node
    print(parent_node)
    print(type(parent_node.next_node))
    cur_node = parent_node
    while cur_node:
        print(cur_node)
        if cur_node.value == 14:
            tmp_node = cur_node.next_node
            cur_node.next_node = LinkedList('9999')
            cur_node.next_node.next_node = tmp_node
        cur_node = cur_node.next_node