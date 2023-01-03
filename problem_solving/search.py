"""
This module implements the state space search algorithm

"""


import sys 
import os
sys.path.append(os.path.abspath("../data_structures"))
from stack import Stack
from n_queens import NQueens

def search(problem):

	# Initialize the frontier with the problem's initial state
	frontier = Stack(problem.initialState)

	# Search
	while True:

		# No solution found
		if frontier.isEmpty():
			return None

		# Select new state to inspect
		state = frontier.pop()

		# Solution found
		if state.isGoal():
			return state

		# Expand state and add new states to frontier
		nextStates = problem.expand(state)
		if nextStates != None:
			frontier.pushItems(nextStates)


# Example usage
if __name__ == '__main__':

	for n in range(1, 9):
		print("N =", n)
		problem = NQueens(n)
		# print(type(problem.initialState.state))
		solution = search(problem)
		if solution == None:
			print("No solution")
		else:
			print(solution.chessCols)
