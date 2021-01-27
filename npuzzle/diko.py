"""
    this file will handle the dictionary that should contain the nodes
"""

class Diko():
	"""
		this class represents the dictionnary
    """

	def __init__(self):
		"""
			constructor
		"""
		self.diko = {}

	def is_puzzle_in(self, puzzle):
		"""
			this method tests if a puzzle is in the dictionary
		"""
		diko = self.diko
		for i in puzzle:
			try:
				diko = diko[i]
			except KeyError:
				return False
		return True

	def add(self, puzzle, open_or_close, f_score, node):
		"""
			this method adds a puzzle to the dictionary
		"""
		diko = self.diko
		elem = 0
		for elem in puzzle:
			olddiko = diko
			try:
				diko = diko[elem]
			except KeyError:
				diko[elem] = {}
				diko = diko[elem]
		olddiko[elem] = [open_or_close, f_score, node]

	def get_puzzle(self, puzzle):
		"""
			this method return the element that corespond to the puzzle
		"""
		diko = self.diko
		for elem in puzzle:
			try:
				diko = diko[elem]
			except KeyError:
				return None
		return diko

	def print_diko(self):
		""" tkt """
		print(self.diko)

if __name__ == "__main__":
	dik = Diko()
	dik.add([0, 1, 2, 3, 5, 4, 6, 7, 8], None, 18, None)
	dik.add([0, 1, 2, 3, 4, 5, 6, 7, 8], None, 17, None)
	if dik.is_puzzle_in([0, 1, 2, 3, 4, 5, 6, 7, 8]):
		print("is_puzzle_in test 1 noice!!")
	if dik.is_puzzle_in([0, 1, 2, 3, 5, 4, 6, 7, 8]):
		print("is_puzzle_in test 2 noice!!")
	if not dik.is_puzzle_in([0, 1, 2, 3, 5, 4, 7, 6, 8]):
		print("is_puzzle_in test 3 noice!!")
	elem1 = dik.get_puzzle([0, 1, 2, 3, 4, 5, 6, 7, 8])
	elem2 = dik.get_puzzle([1, 0, 2, 3, 4, 5, 6, 7, 8])
	print(elem1, elem2)
	dik.print_diko()
