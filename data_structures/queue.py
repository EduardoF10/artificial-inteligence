"""
This module defines the queue data structure

"""


class Node:

	def __init__(self, data):
		self.data = data
		self.next = None


# This class contains a linked list based implementation of queue
class Queue:

	def __init__(self):
		self.front = self.rear = None
		self.currentSize = 0

	def size(self):
		return self.currentSize

	def isEmpty(self):
		return self.size() == 0

	# Method to add an item to the queue
	def enqueue(self, item):
		self.currentSize += 1
		temp = Node(item)
		if self.rear == None:
			self.front = self.rear = temp
		else:
			self.rear.next = temp
			self.rear = temp

	# Method to remove an item from queue
	def dequeue(self):
		if self.isEmpty():
			return None
		else:
			self.currentSize -= 1
			temp = self.front
			self.front = temp.next

			if self.front == None:
				self.rear = None
			return temp.data

	# Method to get all items of the queue in a list
	def getList(self):
		dataList = []
		if self.isEmpty() == False:
			curNode = self.front
			dataList.append(curNode.data)
			for i in range(1, self.size()):
				curNode = curNode.next
				dataList.append(curNode.data)
		return dataList


# Example usage
if __name__ == '__main__':
	queue1 = Queue()
	print("queue1:", queue1.getList())
	print("Size:", queue1.size())
	print("Empty?", queue1.isEmpty())
	queue1.enqueue(40)
	queue1.enqueue(8)
	queue1.enqueue(12)
	queue1.enqueue(23)
	queue1.enqueue(1)
	queue1.enqueue(37)
	queue1.enqueue(4)
	queue1.enqueue(19)
	print("Entered: 40, 8, 12, 23, 1, 37, 4, 19")
	print("queue1:", queue1.getList())
	print("Size:", queue1.size())
	print("Empty?", queue1.isEmpty())
	print("Removed:", queue1.dequeue())
	print("Removed:", queue1.dequeue())
	print("Removed:", queue1.dequeue())
	print("queue1:", queue1.getList())
	print("Size:", queue1.size())
	print("Empty?", queue1.isEmpty())
