"""
This module defines the stack data structure.

"""

class Stack(list):

	def __init__(self, item = None):
		list.__init__(self)
		if item != None:
			self.push(item)

	def push(self, item):
		self.append(item)

	def pushItems(self, itemList):
		self.extend(itemList)

	def pop(self):
		return list.pop(self)

	def peek(self):
		lastItem = self.pop()
		self.push(lastItem)
		return lastItem

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
	stack1.pushItems([2, 5])
	stack1.pushItems([8, 7, 1])
	print("Stack1: [pushItems([2, 5]), pushItems(8, 7, 1)]")
	print("Stack1:", stack1)
