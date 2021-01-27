"""
	docsting
"""

import math

from typing import Any
from typing import List
from typing import Callable

from npuzzle import node
from npuzzle import moves
from npuzzle import usage
from npuzzle.diko import Diko

from npuzzle.constant import debugger
from npuzzle.constant import direction
from npuzzle.constant import solution

def print_puzzle(size, puzzle):
	"""
		this fucntion prints a puzzle
	"""
	for i,val in enumerate(puzzle):
		end = " "
		if not (i + 1) % size:
			end = "\n"
		print("%2d" % val, end=end)
	print("")

class Astar(usage.Manager):
	"""
		Astar
	"""
	@usage.Manager.Decorator.add_durations
	def __init__(
					self,
					size: int,
					puzzle: List[int],
					greedy_algo: [bool, Callable[[int, List[int], List[int]], int]]
	) -> None:
		"""
			constructor
		"""
		usage.Manager.__init__(self)
		self.greedy_algo = greedy_algo
		solution.solution = solution.create_solution(size)
		fst_node = node.Node(
			[size, puzzle],
			None,
			direction.NONE,
			self.greedy_algo
		)
		print_puzzle(size, puzzle)
		self.open = [fst_node]
		self.len_close = 0
		self.diko = Diko()
		self.diko.add(fst_node.puzzle[1], self.open, fst_node.f_score, fst_node)
		self.success_node = None
		self.size = size
		self.stats = {
			"length_open" : len(self.open),
			"length_close" : self.len_close,
			"max" : math.factorial(size**2),
			"time" : 0,
			"size" : 0
		}
		debugger.ASTAR = self

	@usage.Manager.Decorator.add_durations
	def insert_node_in_open(self, noodle):
		"""
			this method insert a node in the open list
		"""
		self.diko.add(noodle.puzzle[1], self.open, noodle.f_score, noodle)
		f_score = noodle.f_score
		l_open = len(self.open)
		start = 0
		l_10 = l_open // 10
		if l_open > 100:
			for i in range(l_open // 10, l_open, l_10):
				if self.open[i].f_score >= f_score:
					start = i - l_10
					break
			if start == 0 and self.open[0].f_score < f_score:
				start = l_open - l_10
			if l_open > 1000:
				start2 = start
				for i in range(start, start + l_10, l_open // 100):
					if self.open[i].f_score >= f_score:
						start2 = i - l_10
						break
				if start2 == start and self.open[start].f_score < f_score:
					start = start + l_10 - l_open // 100
		for i in range(start, l_open):
			if f_score <= self.open[i].f_score:
				self.open.insert(i, noodle)
				return
		self.open.append(noodle)

	@usage.Manager.Decorator.add_durations
	def solve(self) -> None:
		"""
			this method solves the puzzle using A* algorithme
		"""
		success = False
		while not success:
			curr_node = self.open[0]
			self.stats["time"] += 1
			if self.stats["size"] < len(self.open) + self.len_close:
				self.stats["size"] = len(self.open) + self.len_close
			if not curr_node.h_score:
				success = True
				self.success_node = curr_node
			else:
				self.open.remove(curr_node)
				self.len_close += 1
				self.diko.add(
					curr_node.puzzle[1],
					self.len_close,
					curr_node.f_score,
					curr_node
				)
				self._create_children(curr_node)

	@usage.Manager.Decorator.add_durations
	def find_puzzle_in_list(self, noodle: node.Node) -> Any:
		"""
			this method find where (if exists) is a puzzle
			in the open and closed lists
		"""
		element = self.diko.get_puzzle(noodle.puzzle[1])
		if element is None:
			return None, None, None
		if element[0] == self.open:
			return self.open, self.open.index(element[2]), element[2]
		return self.len_close, None, element[2]

	@usage.Manager.Decorator.add_durations
	def _create_children(self, noodle: node.Node) -> None:
		"""
			creates new children from a node
		"""
		direc = [direction.UP, direction.DOWN, direction.RIGHT, direction.LEFT]
		children = [0, 0, 0, 0]
		children[0] = moves.move_up(self.size, noodle.puzzle[1])
		children[1] = moves.move_down(self.size, noodle.puzzle[1])
		children[2] = moves.move_right(self.size, noodle.puzzle[1])
		children[3] = moves.move_left(self.size, noodle.puzzle[1])
		i = -1
		for child in children:
			i += 1
			if child is not None:
				new_node = node.Node(
					[self.size, child],
					noodle,
					direc[i],
					self.greedy_algo
				)
				lists, index, oldnode = self.find_puzzle_in_list(new_node)
				if lists is None:
					self.insert_node_in_open(new_node)
				else:
					if new_node.f_score < oldnode.f_score:
						if lists == self.open:
							del lists[index]
						self.insert_node_in_open(new_node)

	@usage.Manager.Decorator.add_durations
	def show_solve(self):
		"""
			this function show every move from fist state to the solved state
		"""
		directions = [direction.UP, direction.DOWN, direction.RIGHT, direction.LEFT]
		printables = ["UP", "DOWN", "RIGHT", "LEFT"]
		noodle = self.success_node
		tab = []
		while True:
			if noodle.prev_move == direction.NONE:
				break
			tab.insert(0, noodle)
			noodle = noodle.parent
		for nodes in tab:
			i = directions.index(nodes.prev_move)
			print(printables[i])
			print_puzzle(self.size, nodes.puzzle[1])
		print(str(self.success_node.g_score), "moves needed to solve")
		print("Complexity in time: %d" % self.stats['time'])
		print("Complexity in size: %d" % self.stats['size'])

	@usage.Manager.Decorator.add_durations
	def get_stats(self) -> object:
		"""
			docsting
		"""
		self.stats["length_open"] = len(self.open)
		self.stats["length_close"] = self.len_close
		return self.stats
