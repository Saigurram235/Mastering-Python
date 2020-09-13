class Dequeue:
    def __init__(self):
        self.item = []
    def is_empty(self):
        return self.item == []
    def add_front(self, item):
        self.item.append(item)
    def add_rear(self, item):
        self.item.insert(0, item)
    def remove_front(self):
        return self.item.pop()
    def remove_rear(self):
        return self.item.pop(0)
    def size(self):
        return len(self.item)
