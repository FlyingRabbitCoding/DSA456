class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    # T(n) = O (n) = 1

    def is_empty(self) -> bool:
        if self.head is None:
            return True
        else:
            return False
    # T(n) = O (n) = 1

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    # T(n) = O (n) = 1

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None
            current = current.next
        current.next = new_node
    # T (n) = O(n) = n

    def insert_after(self, target: Node, data):
        if target:
            target.next = Node (data, target.next)
    # T(n) = O (n) = 1

    def delete(self, target: Node)->bool:
        if self.head is None:
            return False
        if self.head == target:
            self.head = self.head.next
            return True

        current = self.head
        while current.next:
            if current.next == target:
                current.next = target.next
                return True
            current = current.net
        return False
    # T(n) = O (n) = n

    def search(self, data):
        node = self.head
        while node:
            if node.data == data:
                break
            node = node.next
        return node
    # T(n) = O (n) = n


    def size(self):
        total = 0
        current = self.head
        while current:
            total = total + 1
            current = current.next
        return total
    # T(n) = O (n) = n + 1

    def to_list(self) :
        number_in_list = []
        current = self.head
        while current:
            number_in_list.append(current.data)
            current = current.next
        return number_in_list
    # T(n) = O (n) = n

    def print(self) :
        print(self.to_list())
    # T(n) = O (n) = n

#  part B has been defined after the end of each function