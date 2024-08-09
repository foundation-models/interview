class LinkedList:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
        
a = LinkedList(2)
b = LinkedList(3)
a.next = b

print(a.next.value)
