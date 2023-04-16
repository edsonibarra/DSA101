from src.data_structures.singly_linked_list.node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        cur_node = self.head  # Current node
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        cur_node = self.head
        new_node.next = cur_node
        self.head = new_node

    def print_list(self):
        if self.head is None:
            return
        cur_node = self.head
        while cur_node:
            print(f'[{cur_node.data}]', end='->')
            cur_node = cur_node.next
        print('None')

    def delete_by_value(self, value_to_delete):
        if self.head is None:  # Can't delete a node in an empty linked list
            return
        cur_node = self.head
        prev = None  # previous Node

        # Checks if the first node is the one to delete
        if cur_node.data == value_to_delete:
            self.head = cur_node.next
            cur_node = None
            return

        while cur_node and cur_node.data != value_to_delete:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node:  # If cur_node is None it means wasn't in the linked list
            prev.next = cur_node.next  # Here the Node with value = value_to_delete is deleted.
            cur_node = None
            return

    def delete_by_position(self, position_to_delete):
        if self.head is None:
            return
        cur_node = self.head
        prev = None
        count = 0  # To keep track of the current count

        if position_to_delete == count:
            self.head = cur_node.next
            cur_node = None
            return

        while cur_node and count != position_to_delete:
            count += 1
            prev = cur_node
            cur_node = cur_node.next

        if cur_node:
            prev.next = cur_node.next
            cur_node = None
            return

    def reverse(self):
        if self.head is None:
            return
        cur_node = self.head
        prev = None
        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev  # Here's where the pointer direction is changed
            prev = cur_node
            cur_node = next_node
        self.head = prev

    def merge_sorted_linked_list(self, sorted_linked_list):
        p1 = self.head  # pointer to self.head
        p2 = sorted_linked_list.head  # pointer to the head of sorted_linked_list

        if not p1:
            return p2
        if not p2:
            return p1

        if p1 and p2:
            if p1.data <= p2.data:
                smaller_value = p1
                p1 = smaller_value.next
            else:
                smaller_value = p2
                p2 = smaller_value.next
            new_head = smaller_value
        while p1 and p2:
            if p1.data <= p2.data:
                smaller_value.next = p1
                smaller_value = p1
                p1 = smaller_value.next
            else:
                smaller_value.next = p2
                smaller_value = p2
                p2 = smaller_value.next
        if not p1:
            smaller_value.next = p2
        if not p2:
            smaller_value.next = p1
        self.head = new_head

    def nth_to_last_node(self, n):
        total_len = len(self)
        if n > total_len:
            print(f'n = {n} greater than len of linked list = {total_len}')
            return
        cur_node = self.head
        while cur_node:
            if total_len == n:
                print(f'Nth to last node = {cur_node.data} where n = {n}')
                return cur_node.data
            total_len -= 1
            cur_node = cur_node.next

    def count_occurrences(self, value):
        count = 0
        if self.head is None:
            return count
        cur_node = self.head
        while cur_node:
            if cur_node.data == value:
                count += 1
            cur_node = cur_node.next
        return count

    def node_swap(self, key_1, key_2):
        if key_1 == key_2:
            return

        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def remove_duplicates(self):
        if self.head is None:
            return
        seen_values = {}
        cur_node = self.head
        prev = None
        while cur_node:
            if cur_node.data in seen_values:
                prev.next = cur_node.next
                cur_node = None
            else:
                seen_values[cur_node.data] = True
                prev = cur_node
            cur_node = prev.next

    def rotate(self, k):
        if self.head and self.head.next:
            p = self.head  # it will point to the pivot node
            q = self.head  # it will point to the end node
            count = 0
            prev = None
            while p and count < k:
                count += 1
                prev = p
                p = p.next
            p = prev
            while q:
                prev = q
                q = q.next
            q = prev

            # Rotate
            q.next = self.head
            self.head = p.next
            p.next = None

    def __len__(self):
        count = 0
        if self.head is None:
            return count
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def get_len_recursive(self):
        def _get_len_recursive(node):
            current_node = node
            if current_node is None:
                return 0
            return 1 + _get_len_recursive(current_node.next)
        return _get_len_recursive(self.head)

    def is_palindrome(self, method=1):
        if method == 1:  # Using a string
            values = ""
            cur_node = self.head
            while cur_node:
                values += str(cur_node.data)
                cur_node = cur_node.next
            return values == values[::-1]
        elif method == 2:  # Using a stack
            cur_node = self.head
            values = []
            while cur_node:
                values.append(cur_node.data)
                cur_node = cur_node.next
            cur_node = self.head
            while cur_node:
                data = values.pop()
                if cur_node.data != data:
                    return False
                cur_node = cur_node.next
            return True

    def move_tail_to_head(self):
        cur_node = self.head
        prev = None
        while cur_node.next:
            prev = cur_node
            cur_node = cur_node.next
        first_node = self.head
        prev.next = cur_node.next
        cur_node.next = first_node
        self.head = cur_node


def main():
    linked_list = LinkedList()
    for n in range(1, 5):
        linked_list.append(n)

    linked_list.print_list()
    print(linked_list.get_len_recursive())
    linked_list.nth_to_last_node(2)
    linked_list.nth_to_last_node(1)
    linked_list.nth_to_last_node(4)
    linked_list.nth_to_last_node(5)

    linked_list.rotate(2)
    linked_list.print_list()
    linked_list.move_tail_to_head()
    linked_list.print_list()


if __name__ == "__main__":
    main()
