"""
	use psutil to view memory
"""

import os
import time

import psutil

from npuzzle.constant.debugger import DURATIONS

class Manager:
	"""
		check timer when call a methode
	"""
	def __init__(self):
		"""
			docstring
		"""
		self.memory = 0
		self.free = 0
		if not hasattr(self, "begin"):
			self.begin = 0.0
		if not hasattr(self, "end"):
			self.end = 0.0

	def set_memory_rss(self):
		"""
			[psutil doc](https://psutil.readthedocs.io/en/latest/)

			rss: aka “Resident Set Size”, this is the non-swapped physical      \
			memory a process has used. On UNIX it matches “top“‘s RES column).   \
			On Windows this is an alias for wset field and it matches “Mem Usage” \
			column of taskmgr.exe.

			.. todo:: unit in byte ?
		"""
		self.memory = psutil.Process(os.getpid()).memory_info().rss

	def get_memory_rss(self):
		"""
			return the memory rss
		"""
		return self.memory

	def set_memory_free(self):
		"""
			set the memory available
		"""
		self.free = psutil.virtual_memory().free

	def get_memory_free(self):
		"""
			return the memory available
		"""
		return self.free

	def set_begin(self):
		"""
			docstring
		"""
		self.begin = time.time()

	def set_end(self):
		"""
			docstring
		"""
		self.end = time.time()

	class Decorator:
		"""
			docstring
		"""
		@classmethod
		def add_durations(cls, method):
			"""
				unique decorator
			"""
			def decoration(*args, **kwargs):
				myself = args[0]
				myself.set_begin()
				result = method(*args, **kwargs)
				myself.set_end()
				try:
					DURATIONS["____Total____"] += myself.end - myself.begin
				except KeyError:
					DURATIONS["____Total____"] =  myself.end - myself.begin
				try:
					DURATIONS[f"{type(myself).__name__} : ____Total____"] += \
						myself.end - myself.begin
				except KeyError:
					DURATIONS[f"{type(myself).__name__} : ____Total____"] = \
						myself.end - myself.begin
				try:
					DURATIONS[f"{type(myself).__name__} : {method.__name__}"] += \
						myself.end - myself.begin
				except KeyError:
					DURATIONS[f"{type(myself).__name__} : {method.__name__}"] = \
						myself.end - myself.begin
				return result
			return decoration

		@classmethod
		def useless(cls):
			"""
				it's for pylint...
				R0903: Too few public methods (1/2) (too-few-public-methods)
			"""
			return None
