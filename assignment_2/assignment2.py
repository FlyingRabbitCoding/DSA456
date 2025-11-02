# from assignment_2.a1 import LinkedList


class Node:
    def __init__(self, data, next_node = None, prev_node = None) -> None:
        self.data = data
        self.next = next_node
        self.previous = prev_node

    def get_data(self):
        return self.data

class LinkedList:
    def __init__(self, front=None, back=None) -> None:
        self.head = front
        self.tail = back

    def show(self):
        current_number =  self.head
        while current_number:
            print(current_number.data, end = " -> ")
            current_number = current_number.next

    def get_front(self):
        return None if self.head is None else self.head.data

    def get_back(self):
        return None if self.tail is None else self.tail.data

    def insert_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    def insert_back(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.tail
            self.tail.previous = new_node
            self.tail = new_node

    def insert(self, data):
        new_node = Node(data)
        if self.head is None or data < self.head.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current_data = self.head
            while current_data.next and current_data.next.data < data:
                current_data = current_data.next
            new_node.next = current_data.next
            current_data.next = new_node
    # T(n) = O(n), because it might go through the whole list

    def remove(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.previous:
                    current.previous.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.previous = current.previous
                else:
                    self.tail = current.previous
                return True
            current = current.next
        return False

    # T(n) = O(n), because it might go through the whole list


    def is_present(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        print("this number is no in the list")
        return False
    # T(n) = O(n), because it might go through the whole list


    def __len__(self):
        count = 0
        current = self.head
        while current:
            count = count + 1
            current = current.next
        return count
    # T(n) = O(n), because it might go through the whole list



n1 = Node("55")

n2 = Node("56")
n2.previous = n1
n3 = Node("57")
n2.next = n3
n1.next = n2
n1.previous = None
n3. previous = n2


l3 = LinkedList(n1)
# print(l3.show())
ll = LinkedList()
ll.insert(30)
ll.insert(10)
ll.insert(20)
ll.remove(10)

print(ll.show())
print(ll.is_present(40))
print(len(ll))

# Part C analysis:
# all 4 functions are # T(n) = O(n), because it might go through the whole list