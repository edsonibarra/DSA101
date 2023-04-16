def traverse_linked_list(linked_list):
    current_node = linked_list.head
    values = []
    while current_node:
        values.append(current_node.data)
        current_node = current_node.next
    return values
