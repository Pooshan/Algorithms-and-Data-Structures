class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
                                                                        
q = Queue()


q.size()
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.size())

q.size()
q.isEmpty()
q.enqueue(8.4)
q.dequeue()
q.dequeue()
q.size()
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.size())

