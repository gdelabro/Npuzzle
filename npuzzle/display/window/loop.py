"""
	test thread
"""

import tkinter

from npuzzle.display import debug
from npuzzle.constant import debugger

def update_windows(window, lbl, duration) -> None:
	"""
		Update the text in the Debugger's informations
	"""
	data = debug.Informations()
	if debugger.ASTAR is not None:
		new_infos = data.get_all(debugger.ASTAR)
	lbl.config(text=new_infos)
	window.after(duration, update_windows, window, lbl, duration)

def threader() -> None:
	"""
		docstring
	"""
	window = tkinter.Tk()
	window.title("Debugger's informations")
	window.configure(background="black")
	lbl = tkinter.Label(
		window,
		text="...",
		bg="black",
		fg="white",
		font="TkFixedFont",
		justify=tkinter.LEFT
	)
	lbl.pack()
	duration = 1000
	window.after(duration, update_windows, window, lbl, duration)
	window.mainloop()
