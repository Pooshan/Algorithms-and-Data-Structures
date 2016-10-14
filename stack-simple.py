
class Stack:
  
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
s = Stack()


print(s.isEmpty())
s.push('dog')
s.push(4)
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())

"""
------
Output:

Pooshans-MacBook-Pro:Algorithms & Data Structures Pooshan$ python3 stack-simple.py 
True
4
3
False
8.4
True
2
Pooshans-MacBook-Pro:Algorithms & Data Structures Pooshan$ 
-------
"""

