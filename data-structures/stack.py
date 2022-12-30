"""
This module defines the stack data structure.

"""

class Stack(list):

	def push(self, item):
		self.append(item)

	def pop(self):
		return list.pop(self)

	def isEmpty(self):
		return len(self) == 0


# Example usage

if __name__ == '__main__':
	stack = Stack()
	print(stack.isEmpty())
	stack.push(7)
	print(stack.isEmpty())
	print(stack.pop())
	print(stack.isEmpty())

