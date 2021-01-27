"""
	this file is the parsing part of the program
	and also checks if the puzzle is solvable
"""
import sys
from npuzzle.constant import solution

def usage(strerr = None) -> None:
	"""
		this method show the usage to the user
	"""
	if strerr is not None:
		print (strerr)
	print ("usage: python3 app.py file [options ..]\noptions:")
	print ("\t--heuristic=manhattan/euclidian/notinplace")
	print ("\t--greedy\n\t--debug\n\t--debug_mod=log/window/console")
	sys.exit()

def open_file(filename):
	"""
		this function opens a file name filename and returns it

		:raises: raises error if it cannot open the file
	"""
	try:
		filedescriptor = open(filename, "r")
	except FileNotFoundError:
		usage("no such file or directory")
	except IsADirectoryError:
		usage(filename + " is a directory")
	except PermissionError:
		usage(filename + " permission denied")
	return filedescriptor

class Parser():
	"""
		this class is used to pars the puzzle from a file
	"""
	def __init__(self, filename) -> None:
		"""
			constructor
		"""
		filename = open_file(filename)
		self.size_filled = 0
		self.puzzle = []
		for line in filename.readlines():
			line = line.split("#")[0]
			if not line.split():
				continue
			if not self.size_filled:
				self.size_filled = 1
				if len(line.split()) != 1:
					usage("bad size of the puzzle")
				try:
					self.size = int(line.split()[0])
				except ValueError:
					usage("puzzle size isn't a number")
			else:
				if len(line.split()) != self.size:
					usage("a line of the puzzle has not the good size")
				for i in line.split():
					try:
						self.puzzle.append(int(i))
					except ValueError:
						usage("an element isn't a number")
		if len(self.puzzle) != self.size ** 2:
			usage("puzzle doesn't have the good number of element")
		self.solution = solution.create_solution(self.size)
		self.check_valid_puzzle()
		if not self.check_if_solvable():
			usage("puzzle isn't solvable")

	def check_valid_puzzle(self) -> None:
		"""
			this method checks if the puzzle has the right elements in it
		"""
		verif = [0 for i in range(0, self.size ** 2)]
		for i in self.puzzle:
			if i < 0 or i >= self.size ** 2:
				usage("number out of range in the puzzle")
			verif[i] = 1
		for i in verif:
			if not i:
				usage("not every number is in the puzzle")

	def is_inverted(self, element1, element2) -> bool:
		"""
			this method checks if two elements are inverted
		"""
		if not element1 or not element2:
			return 0
		for i in range(0, self.size ** 2):
			element = self.solution[i]
			if element in (element1, element2):
				return 0 if element == element1 else 1
		return 1

	def check_if_solvable(self) -> bool:
		"""
			this method checks if the puzzle is solvable
		"""
		inversions = 1
		for i in range(0, self.size ** 2):
			for j in range(i + 1, self.size ** 2):
				if self.is_inverted(self.puzzle[i], self.puzzle[j]):
					inversions += 1
		if self.size % 2 == 1:
			return inversions % 2
		for i in range(0, self.size ** 2):
			if not self.solution[i]:
				row1 = int(i / self.size)
			if not self.puzzle[i]:
				row2 = int(i / self.size)
		return (inversions + row1 + row2) % 2
