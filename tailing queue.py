class MyQueue(object):
    def __init__(self):
        self.stack2 = []
        
    
    def peek(self):
        if len(self.stack2) != 0:
            return self.stack2[0]
       
        
    def pop(self):
        if len(self.stack2) != 0:
            return self.stack2.pop(0)

        
    def put(self, value):
        self.stack2.append(value)
            
queue = MyQueue()
queue.put(42)
queue.pop()

queue.put(14)
queue.peek()

# t = int(input())
# for line in range(t):
#     values = map(int, input().split())
#     values = list(values)
#     if values[0] == 1:
#         queue.put(values[1])        
#     elif values[0] == 2:
#         queue.pop()
#     else:
#         print(queue.peek())
