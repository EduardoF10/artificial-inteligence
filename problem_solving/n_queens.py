"""
This module defines the n-queens class.

"""



import sys 
import os
sys.path.append(os.path.abspath("../data_structures"))
from stack import Stack

class NQueens:

	def __init__(self, n):
		self.initialState = self.State([None] * n)

	def expand(self, state):

		chessCols = state.chessCols

		if state == None:
			return None

		possibleRows = set(range(len(chessCols)))

		# Getting first empty column index
		for i in range(len(chessCols)):
			if chessCols[i] == None:
				colIndex = i
				break
				
		# Discarding invalid rows
		for col in range(colIndex):
			# Horizontally
			possibleRows.discard(chessCols[col])
			# Diagonally
			possibleRows.discard(chessCols[col] + (colIndex - col))
			possibleRows.discard(chessCols[col] - (colIndex - col))

		if len(possibleRows) == 0:
			return None
		else:
			states = []
			for row in possibleRows:
				newCols = list(chessCols)
				newCols[colIndex] = row
				states.append(self.State(newCols))
		return states

	def viewStates(stateList):
		if stateList == None or len(stateList) == 0:
			return None
		if len(stateList) == 1:
			return "[" + str(stateList[0].chessCols) + "]"
		result = "["
		for i in range(len(stateList) - 1):
			result += str(stateList[i].chessCols) + ", "
		result += str(stateList[-1].chessCols) + "]"
		return result


	class State:

		def __init__(self, cols = None):
			self.chessCols = cols

		def isGoal(self):
			if self.chessCols == None:
				return False
			return self.chessCols[len(self.chessCols) - 1] != None


# Example usage
if __name__ == '__main__':
	pass
			