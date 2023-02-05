class Queue:
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)

    def pop(self):
        return self.list.pop(0)

    def is_empty(self):
        return not self.list


# queue = Queue()
# for item in ("Hello,", "world!"):
#     queue.push(item)
# while not queue.is_empty():
#     print(queue.pop())

