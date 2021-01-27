"""
	this file move the tuils on the puzzle
"""

from typing import List

def move_up(size: int, puzzle: List[int]) -> List[int]:
	"""
		it moves the 0 tuil up
	"""
	puzzle2 = puzzle.copy()
	i = puzzle.index(0)
	if not i // size:
		return None
	puzzle2[i], puzzle2[i - size] = puzzle[i - size], puzzle[i]
	return puzzle2

def move_down(size: int, puzzle: List[int]) -> List[int]:
	"""
		it moves the 0 tuil down
	"""
	puzzle2 = puzzle.copy()
	i = puzzle.index(0)
	if i // size == size - 1:
		return None
	puzzle2[i], puzzle2[i + size] = puzzle[i + size], puzzle[i]
	return puzzle2

def move_right(size: int, puzzle: List[int]) -> List[int]:
	"""
		it moves the 0 tuil down
	"""
	puzzle2 = puzzle.copy()
	i = puzzle.index(0)
	if i % size == size - 1:
		return None
	puzzle2[i], puzzle2[i + 1] = puzzle[i + 1], puzzle[i]
	return puzzle2

def move_left(size: int, puzzle: List[int]) -> List[int]:
	"""
		it moves the 0 tuil down
	"""
	puzzle2 = puzzle.copy()
	i = puzzle.index(0)
	if not i % size:
		return None
	puzzle2[i], puzzle2[i - 1] = puzzle[i - 1], puzzle[i]
	return puzzle2
