"""
This module defines the linked list data structure.

"""

class Node:

	def __init__(self, dataVal = None, nextNode = None):
		self.dataVal = dataVal
		self.nextNode = nextNode


class SLinkedList:

	# SLinkedList can be intialized with a data value or a list of data values
	def __init__(self, dataVal = None):
		if dataVal == None:
			self.headNode = None
			self.currentSize = 0
		elif type(dataVal) != list:
			self.headNode = Node(dataVal)
			self.currentSize = 1
		else:
			self.headNode = Node(dataVal[0])
			self.currentSize = len(dataVal)
			curNode = self.headNode
			for i in range(1, len(dataVal)):
				nodeI = Node(dataVal[i])
				curNode.nextNode = nodeI
				curNode = curNode.nextNode

	def size(self):
		return self.currentSize

	def isEmpty(self):
		return self.size() == 0


	def get(self, index):
		if index < 0 or index > self.size():
			return None
		else:
			curNode = self.headNode
			for i in range(1, index + 1):
				curNode = curNode.nextNode
			return curNode


	def add(self, dataVal, index = None):
		if index == None:
			index = self.size()
		if index == 0:
			self.headNode = Node(dataVal, self.headNode)
		else:
			self.get(index - 1).nextNode = Node(dataVal, self.get(index))
		self.currentSize += 1


	def removeAt(self, index):
		removedElem = None
		if index < 0:
			index = self.currentSize + index
		if index == 0:
			removedElem = self.headNode
			self.headNode = removedElem.nextNode
		else:
			removedElem = self.get(index)
			self.get(index - 1).nextNode = removedElem.nextNode
		self.currentSize -= 1
		return removedElem


	def getList(self):
		dataList = []
		if self.isEmpty() == False:
			curNode = self.headNode
			dataList.append(curNode.dataVal)
			for i in range(1, self.size()):
				curNode = curNode.nextNode
				dataList.append(curNode.dataVal)
		return dataList
		

# Example usage
if __name__ == '__main__':
	linkedList1 = SLinkedList()
	print("linkedList1:", linkedList1.getList())
	print("Size:", linkedList1.size())
	print("Empty?", linkedList1.isEmpty())
	linkedList1.add(4, 0)
	linkedList1.add(1, 0)
	linkedList1.add(7)
	linkedList1.add(2)
	linkedList1.add(12, 1)
	print("linkedList1: [add(4, 0), add(1, 0), add(7), add(2), add(12, 1)]")
	print("linkedList1:", linkedList1.getList())
	print("Size:", linkedList1.size())
	print("Empty?", linkedList1.isEmpty())
	linkedList1.removeAt(2)
	linkedList1.removeAt(-1)
	print("linkedList1: [removeAt(2), removeAt(-1)]")
	print("linkedList1:", linkedList1.getList())
	print("Size:", linkedList1.size())
	print("Empty?", linkedList1.isEmpty())
