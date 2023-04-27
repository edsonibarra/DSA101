from src.data_structures.circular_linked_list.node import Node


class CicularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """
        Appending to a Circular Linked List implies inserting the new Node after the node that
        was previously pointing to the head of the linked list.

        - append to an empty circular linked list:
        If you want to append to an empty circular linked list, the first thing to do is to create the new node.
        After, assign the new node to self.head variable and make it point to itself.
        This logic will be used later for appending a new node when the linked list is not empty.

        
        """
        new_node = Node(data)
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = new_node
            new_node.next = self.head
        
    def print_list(self):
        if self.head is None:
            return
        current_node = self.head
        while current_node is not self.head:
            print(f"[{current_node.data}]", end="->")
            current_node = current_node.next
        print("None")
    

def main():
    cll = CicularLinkedList()
    cll.append(1)
    cll.print_list()


main()