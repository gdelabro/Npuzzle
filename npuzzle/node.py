"""
	docsting
"""

from typing import Any
from typing import List
from typing import Callable

from npuzzle import usage
from npuzzle.constant import solution

class Node(usage.Manager):
	"""
		This Class represent a Node.
		A node is one state of a N-puzzle.
	"""
	@usage.Manager.Decorator.add_durations
	def __init__(
					self,
					puzzle: [int, List[int]],
					parent: Any,
					prev_move: int,
					greedy_algo: [bool, Callable[[int, List[int], List[int]], int]]
	) -> None:
		"""
			constructor

			:raises: ValueError("...") if the puzzle doesn't fit in the size given
		"""
		usage.Manager.__init__(self)
		if len(puzzle[1]) != (puzzle[0] ** 2):
			raise ValueError(
				f"The puzzle's size is {len(puzzle[1])}, it should be {puzzle[0] ** 2} : "
				f"{puzzle[1]}".replace('[', '').replace(']', '')
			)
		self.puzzle = puzzle
		self.parent = parent
		self.prev_move = prev_move
		self.greedy_algo = greedy_algo
		self.g_score = self.set_g()
		self.h_score = self.set_h(puzzle[0])
		if self.greedy_algo[0] is False:
			self.f_score = self.g_score + self.h_score
		else:
			self.f_score = self.h_score

	@usage.Manager.Decorator.add_durations
	def set_g(self) -> int:
		"""
			The method _g(self) is the "cost" of the node (self)
		"""
		if self.parent is None:
			return 0
		return self.parent.g_score + 1

	@usage.Manager.Decorator.add_durations
	def set_h(self, size) -> int:
		"""
			The method set_h(self) is the "calculated heuristic" of the node (self)
		"""
		return self.greedy_algo[1](size, self.puzzle[1], solution.solution)

	@usage.Manager.Decorator.add_durations
	def get_g_score(self) -> int:
		"""
			gives the g score
		"""
		return self.g_score

	@usage.Manager.Decorator.add_durations
	def val_h(self) -> int:
		"""
			gives the h score
		"""
		return self.h_score

	@usage.Manager.Decorator.add_durations
	def get_f_score(self) -> int:
		"""
			gives the f score
		"""
		return self.f_score
