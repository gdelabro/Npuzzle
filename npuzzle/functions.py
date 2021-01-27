"""
    docsting
"""

import math

from typing import List

def manhattan(size: int, puzzle: List[int], solution: List[int]) -> int:
	"""
		this is the manhattan heuristic function to calculate _h
	"""
	res = 0
	for i in range(1, size ** 2):
		index1 = puzzle.index(i)
		index2 = solution.index(i)
		dist = abs(index1 % size - index2 % size)+abs(index1 // size - index2 // size)
		res += dist
	return res

def euclidian(size: int, puzzle: List[int], solution: List[int]) -> int:
	"""
		this is the euclidian heuristic function to calculate _h
	"""
	res = 0
	for i in range(1, size ** 2):
		index1 = puzzle.index(i)
		index2 = solution.index(i)
		dist = math.sqrt(abs(index1 % size - index2 % size) ** 2 +\
			abs(index1 // size - index2 // size) ** 2)
		res += dist
	return res

def not_in_place(size: int, puzzle: List[int], solution: List[int]) -> int:
	"""
		this is the not in place heuristic function to calculate _h
	"""
	res = 0
	for i in range(1, size ** 2):
		if puzzle.index(i) != solution.index(i):
			res += 1
	return res
