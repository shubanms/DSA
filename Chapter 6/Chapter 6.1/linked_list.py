import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Called function {} and it took {:.6f} sec to execute\n".format(func.__name__, end-start))
    return wrapper

class Node:
    def __init__(self, value, next = None) -> None:
        self.value = value
        self.next = next
        
class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    @timer
    def print_linked_list(self) -> None:
        if self.head is None:
            print("None")
            return
        else:
            iterator, linked_list_values = self.head, ""
            
            while iterator:
                linked_list_values += str(iterator.value) + " --> "
                iterator = iterator.next
                
            linked_list_values += "None"
            
            print(linked_list_values)

    @timer
    def length(self) -> None:
        if self.head is None:
            print("Length of the linked list is 0")
        else:
            iterator = self.head
            count = 0
            
            while iterator:
                count += 1
                iterator = iterator.next
                
            print("Length of the linked list is {}".format(count))
        
    def insert(self, value) -> None:
        node = Node(value)
        
        if self.head is None:
            self.head = node
            return
        else:
            node.next = self.head
            self.head = node
            return
    
    def append(self, value) -> None:
        node = Node(value)
        
        if self.head is None:
            self.head = node
            return
        else:
            iterator = self.head
            
            while iterator.next:
                iterator = iterator.next
                
            iterator.next = node
            return
        
    def remove_head(self) -> None:
        if self.head is None:
            return
        else:
            self.head = self.head.next
            return
        
    def remove_tail(self) -> None:
        if self.head is None:
            return
        else:
            iterator = self.head
            
            if iterator.next is None:
                self.head = None
                return
            
            while iterator.next.next:
                iterator = iterator.next

            iterator.next = None
            return
        
    @timer
    def find_element(self, value) -> None:
        if self.head is None:
            return
        else:
            iterator = self.head
            
            while iterator:
                if iterator.value == value:
                    print("Element found!")
                    return
                else:
                    iterator = iterator.next

            print("Element not found!")
            
    def delete_element(self, value) -> None:
        if self.head is None:
            return
        else:
            iterator, forward = self.head, self.head
            
            while iterator.next:
                if iterator.next.value == value:
                    break
                else:
                    forward = forward.next
                    iterator = iterator.next
                    
            if iterator.next is None:
                self.head = None
                return
            
            forward = forward.next.next
            iterator.next = forward
            
            return
    
ll = LinkedList()

ll.insert(1)
ll.insert(2)
ll.print_linked_list()

ll.remove_tail()
ll.print_linked_list()

ll.remove_tail()
ll.print_linked_list()

ll.insert(3)
ll.insert(4)
ll.print_linked_list()

ll.length()

ll.insert(5)
ll.print_linked_list()

ll.append(0)
ll.print_linked_list()

ll.remove_head()
ll.print_linked_list()

ll.find_element(1)

ll.delete_element(3)
ll.print_linked_list()

ll.delete_element(0)
ll.print_linked_list()

ll.delete_element(4)
ll.print_linked_list()