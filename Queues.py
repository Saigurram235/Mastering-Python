

class Queue:
    def __init__(self):
        self.item = []

    def enqueue(self, item):
        return self.item.insert(0, item)

    def dequeue(self):
        return self.item.pop()

    def is_empty(self):
        return self.item == []

    def size(self):
        return len(self.item)


# q = Queue()
# print(q.is_empty())
# q.enqueue(45)
# q.enqueue(75)
# print(q.size())
# print(q.is_empty())
# print(q.dequeue())


