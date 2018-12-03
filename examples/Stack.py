#!/usr/bin/env python
Program := Stack

class Stack:
     def __init__(self) =
        self.items = []

     def isEmpty(self) =
        return self.items == []

     def push(self, item) =
        self.items.append(item)

     def pop(self) =
        return self.items.pop()

     def peek(self) =
        return self.items[len(self.items)-1]

     def size(self) =
        return len(self.items)

     def __del__(self) =
        print('destroying stack')


s = Stack()

s.push('a')
s.push('b')
s.push('c')

# returns 3
num := s.size()
# Returns top element
topElement = s.peek()
# Returns last element in the stack
element := s.pop()
