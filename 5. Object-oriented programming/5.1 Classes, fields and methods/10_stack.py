class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop(-1)

    def is_empty(self):
        return not self.stack


# stack = Stack()
# for item in ("Hello,", "world!"):
#     stack.push(item)
# while not stack.is_empty():
#     print(stack.pop())
