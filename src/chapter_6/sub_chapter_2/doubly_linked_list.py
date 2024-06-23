import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Called function {} and it took {:.6f} sec to execute\n".format(
            func.__name__, end-start))
        return result
    return wrapper


class Node:
    def __init__(self, value, next=None, prev=None) -> None:
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None

    @timer
    def print(self) -> None:
        if self.head is None:
            print("None")
            return
        else:
            iterator, linked_list_values = self.head, "None <--> "

            while iterator:
                linked_list_values += str(iterator.value) + " <--> "
                iterator = iterator.next

            linked_list_values += "None"

            print(linked_list_values)

    def insert(self, value) -> None:
        node = Node(value)

        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def append(self, value) -> None:
        node = Node(value)

        if self.head is None:
            self.head = node
        else:
            iterator = self.head

            while iterator.next:
                iterator = iterator.next

            node.prev = iterator
            iterator.next = node

    def reverse(self) -> None:
        current = self.head
        temp = None

        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

        if temp:
            self.head = temp.prev

    def delete(self, value) -> None:
        if self.head is None:
            return
        else:
            iterator = self.head

            while iterator:
                if iterator.value == value:
                    break
                else:
                    iterator = iterator.next

            iterator.prev.next = iterator.next

            return


dll = DoublyLinkedList()

dll.insert(1)
dll.insert(2)
dll.insert(3)
dll.insert(4)
dll.insert(5)
dll.print()

dll.append(0)
dll.print()

dll.reverse()
dll.print()

dll.delete(4)
dll.print()
