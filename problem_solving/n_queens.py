"""
This module defines the n-queens class.

"""


def viewStates(stateList):
	if stateList == None or len(stateList) == 0:
		return None
	if len(stateList) == 1:
		return "[" + str(stateList[0].state) + "]"
	result = "["
	for i in range(len(stateList) - 1):
		result += str(stateList[i].state) + ", "
	result += str(stateList[-1].state) + "]"
	return result


class State:

	def __init__(self, state = None):
		self.state = state

	def getState(self):
		return self.state

	def nextStates(self):
		if self.state == None:
			return None

		possibleRows = set(range(len(self.state)))

		# Getting first empty column index
		for i in range(len(self.state)):
			if self.state[i] == None:
				colIndex = i
				break


		# Discarding invalid rows
		for col in range(colIndex):
			# Horizontally
			possibleRows.discard(self.state[col])
			# Diagonally
			possibleRows.discard(self.state[col] + (colIndex - col))
			possibleRows.discard(self.state[col] - (colIndex - col))

		if len(possibleRows) == 0:
			return None
		else:
			states = []
			for row in possibleRows:
				newState = list(self.state)
				newState[colIndex] = row
				states.append(State(newState))
		return states


import sys 
import os
sys.path.append(os.path.abspath(".."))
from data_structures import stack

class NQueens:

	def __init__(self, n):
		self.initialState = State([None] * n)

	def isGoal(self, stateObj):
		return stateObj.state[n - 1] != None


	



class Main():

	def __init__(self, problem):
		self.problem = problem
		self.frontier = stack.Stack([problem.initialState])

	def search(self):
		while True:
			# Frontier is empty; no solution
			if self.frontier.isEmpty():
				return None

			# Pop state from frontier
			state = self.frontier.pop()

			# State contains goal; solution
			if self.problem.isGoal(state):
				return state

			# Expand next states
			nextStates = state.nextStates()
			if nextStates != None:
				self.frontier.pushItems(nextStates)


# Example usage
if __name__ == '__main__':

	for n in range(1, 9):
		print("N =", n)
		problem = NQueens(n)
		searchAlgorithm = Main(problem)

		solution = searchAlgorithm.search()
		if solution == None:
			print("No solution")
		else:
			print(solution.state)
			