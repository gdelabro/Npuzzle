"""
	this file is the main file of the application
"""

import sys
import threading

from typing import List
from typing import Callable

import npuzzle

def choose_debugger(word: str) -> Callable[[int, List[int], List[int]], int]:
	"""
		choose the debugger between log, window and console
	"""
	if word in ("log", "0"):
		debug_mod = npuzzle.display.log.loop.threader
	elif word in ("window", "1"):
		debug_mod = npuzzle.display.window.loop.threader
	elif word in ("console", "2"):
		debug_mod = npuzzle.display.console.loop.threader
	else:
		debug_mod = None
	return debug_mod

def pars_options(args):
	"""
		this function pars the options from the args
	"""
	heuristics = npuzzle.heuristic.Heuristic()
	file2open = None
	is_debug_on = False
	debug_mod = None#npuzzle.display.log.loop.threader
	is_greedy_on = False
	skip = True
	for arg in args:
		if skip is True:
			skip = False
			continue
		words = arg.split("=")
		if arg == "--greedy":
			is_greedy_on = 1
		elif len(words) == 2 and words[0] == "--heuristic":
			i = 0
			for fun in heuristics.functions:
				if words[1].lower() in (str(i), fun.__name__):
					heuristics.set_identifiant(i)
					break
				i += 1
		elif len(words) == 2 and words[0] == "--debug":
			debug_mod = choose_debugger(words[1].lower())
		else:
			if file2open is None:
				file2open = arg
			else:
				msg = f"Argument {arg} is invalide. "
				msg += "Please use greedy, heuristic, debug or debug_mod as options"
				raise Exception(msg)
	if file2open is None:
		npuzzle.parsing.usage("filename needed")
	if debug_mod is not None:
		is_debug_on = True
	return file2open, is_greedy_on, heuristics, is_debug_on, debug_mod

if __name__ == "__main__":
	filename, greedy, function, debug, debugger_mod = pars_options(sys.argv)
	if debug is True:
		debugger = threading.Thread(
			target=debugger_mod,
			args=()
		)
		debugger.daemon = True
		debugger.start()
	pars = npuzzle.parsing.Parser(filename)
	astar = npuzzle.astar.Astar(
		pars.size,
		pars.puzzle,
		[greedy, function.get_function()]
	)
	astar.solve()
	astar.show_solve()
