"""
	test thread
"""

import os
import time

from npuzzle.display import debug
from npuzzle.constant import debugger

def threader() -> None:
	"""
		docstring
	"""
	while True:
		os.system("clear")
		data = debug.Informations()
		if debugger.ASTAR is not None:
			print(data.get_all(debugger.ASTAR))
		time.sleep(1)
