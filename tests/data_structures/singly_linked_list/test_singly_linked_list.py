from src.data_structures.singly_linked_list.singly_linked_list import LinkedList
from tests.data_structures.singly_linked_list.utils import traverse_linked_list


def test_merge_sorted_linked_list_same_length():
    # Create first sorted linked list
    linked_list = LinkedList()
    linked_list.append(32)
    linked_list.append(544)
    linked_list.append(33000)

    all_values = []
    cur_node_1 = linked_list.head
    while cur_node_1:
        all_values.append(cur_node_1.data)
        cur_node_1 = cur_node_1.next

    # Create second sorted linked list
    linked_list_2 = LinkedList()
    linked_list_2.append(21)
    linked_list_2.append(444)
    linked_list_2.append(500000)

    cur_node_2 = linked_list_2.head
    while cur_node_2:
        all_values.append(cur_node_2.data)
        cur_node_2 = cur_node_2.next

    # Merge linked_list_2 into linked_list
    linked_list.merge_sorted_linked_list(linked_list_2)

    # Get the values of the merged linked list
    merged_ll_values = traverse_linked_list(linked_list)

    assert merged_ll_values == sorted(all_values)
    assert len(linked_list) == 6


def test_remove_duplicates():
    linked_list = LinkedList()
    for n in range(1, 4):
        linked_list.append(n)
        linked_list.append(n)
        linked_list.append(n)
        linked_list.append(n)
        linked_list.append(n)
    linked_list.print_list()
    linked_list.remove_duplicates()
    linked_list.print_list()
    expected = [1, 2, 3]
    values = traverse_linked_list(linked_list)
    assert expected == values


def test_is_palindrome():
    linked_list = LinkedList()
    palindrome = 'kayak'
    for c in palindrome:
        linked_list.append(c)

    assert linked_list.is_palindrome(method=2) is True
    assert linked_list.is_palindrome(method=1) is True