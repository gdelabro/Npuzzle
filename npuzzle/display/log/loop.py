"""
	test thread
"""

import time

from npuzzle.display import debug
from npuzzle.constant import debugger

def threader() -> None:
	"""
		docstring
	"""
	while True:
		data = debug.Informations()
		if debugger.ASTAR is not None:
			logfile = open("./npuzzle.html", "w")
			logfile.write("<p style=\"font:Courier New;white-space:pre\">")
			logfile.write(data.get_all(debugger.ASTAR))
			logfile.write("</p>\n")
			logfile.close()
			time.sleep(1)
