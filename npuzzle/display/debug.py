"""
	docstring
"""

import json
from typing import Any

from npuzzle import usage
from npuzzle.constant.debugger import DURATIONS

class Informations:
	"""
		docstring
	"""
	def __init__(self):
		self._set_progress_bar("init", 100, 100)

	def _set_progress_bar(self, name: str, current: int, maximun: int) -> None:
		"""
			docstring
		"""
		percent = int(100*current/maximun)
		self.progress_bar = f"\n {name:10} : {percent:3} % : ["
		for index in range (50):
			if (2*index) >= percent:
				self.progress_bar += ' '
			elif (2*index) == (percent-1):
				self.progress_bar += '.'
			else:
				self.progress_bar += ':'
		self.progress_bar += f"] : {current:30} / {maximun}"

	def _get_progress_bar(self) -> str:
		"""
			docstring
		"""
		return self.progress_bar

	def get_all(self, tree: Any):
		"""
			docstring
		"""
		return self.get_memory() + self.get_open(tree) + \
			self.get_close(tree) + self.get_node(tree) + \
			get_timers()

	def get_memory(self):
		"""
			docstring
		"""
		manager = usage.Manager()
		manager.set_memory_rss()
		manager.set_memory_free()
		self._set_progress_bar(
			"memory",
			manager.get_memory_rss(),
			manager.get_memory_rss() + manager.get_memory_free()
		)
		return self._get_progress_bar()

	def get_node(self, tree: Any):
		"""
			docstring
		"""
		stats = tree.get_stats()
		self._set_progress_bar(
			"node",
			stats["length_open"] + stats["length_close"],
			stats["max"]
		)
		return self._get_progress_bar()

	def get_open(self, tree: Any):
		"""
			docstring
		"""
		stats = tree.get_stats()
		self._set_progress_bar(
			"open",
			stats["length_open"],
			stats["length_open"] + stats["length_close"]
		)
		return self._get_progress_bar()

	def get_close(self, tree: Any):
		"""
			docstring
		"""
		stats = tree.get_stats()
		self._set_progress_bar(
			"close",
			stats["length_close"],
			stats["length_open"] + stats["length_close"]
		)
		return self._get_progress_bar()

def get_timers() -> str:
	"""
		docstring
	"""
	return f"\n DURATIONS = {json.dumps(DURATIONS, sort_keys=True, indent=4)}"
