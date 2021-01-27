"""
	docstring
"""

from typing import List
from typing import Callable

from npuzzle import functions

class Heuristic:
	"""
		a class where are stock different type of heuristic function
	"""
	def __init__(self) -> None:
		self.identifiant = 0
		self.functions = [
			functions.manhattan,
			functions.euclidian,
			functions.not_in_place
		]

	def set_identifiant(self, identifiant: int) -> None:
		"""
			set a new identifiant
		"""
		self.identifiant = identifiant
		if self.identifiant < 0 or self.identifiant > len(self.functions):
			msg = f"The identifiant {self.identifiant} is out of range :" + \
				f"[0-{len(self.functions)}]"
			raise IndexError(msg)

	def get_identifiant(self) -> int:
		"""
			return the identifiant of the function use
		"""
		return self.identifiant

	def get_function(self) -> Callable[[int, List[int], List[int]], int]:
		"""
			retourn the function link to identifiant
		"""
		return self.functions[self.get_identifiant()]
