class Stack():
    def __init__(self):
        self.stack = []
        self.n = 0
    
    def pop(self):
        if self.is_empty():
            return None
        else:
            self.n -= 1
            return self.stack[self.n]

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack[self.n - 1]

    def is_empty(self):
        return self.n == 0

    def push(self, x):
        self.stack.append(x)
        self.n += 1

    def print(self):
        n = self.n
        print("Stack: ")
        print('[', end="")
        for i in range(0, n):
            if i == n - 1:
                print(self.stack[i], end="")
            else:
                print(i, end=", ")
        print("]")



# s = Stack()
# for i in range(0, 20, 2):
#     s.push(i)
#     if i % 3 == 0:
#         x = s.pop()
#         print(i, x)
#     if i % 5 == 0:
#         x = s.peek()
#         print(i, x)

# s.print()


