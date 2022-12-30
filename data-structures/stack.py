"""
This module defines the stack data structure.

"""

class Stack(list):

	def __init__(self, iterable = None):
		if iterable == None:
			list.__init__(self)
		else:
			list.__init__(self, iterable)

	def push(self, item):
		self.append(item)

	def pop(self):
		return list.pop(self)

	def isEmpty(self):
		return len(self) == 0

	def size(self):
		return len(self)


# Example usage
if __name__ == '__main__':
	stack1 = Stack()
	stack2 = Stack([3, 7, 4])
	print("Stack1:", stack1)
	print("Stack2:", stack2)
	print("Stack1 is empty?", stack1.isEmpty())
	print("Stack2 is empty?", stack2.isEmpty())
	stack1.push(3)
	stack1.push(4)
	stack1.pop()
	stack1.push(7)
	print("Stack1: [(push, 3), (push, 4), (pop), (push, 7)]")
	print("Stack1:", stack1)
	stack2.push(1)
	stack2.pop()
	stack2.pop()
	stack2.push(9)
	print("Stack2:[(push, 1), (pop), (pop), (push, 9)]")
	print("Stack2:", stack2)
	print("Stack1 size:", stack1.size())
	print("Stack2 size:", stack2.size())
	print("Stack1 is empty?", stack1.isEmpty())
	print("Stack2 is empty?", stack2.isEmpty())
