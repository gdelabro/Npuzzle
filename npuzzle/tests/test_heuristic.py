"""
	docstring
"""

import pyclbr

from npuzzle import heuristic

def test_init__functions():
	"""
		Count all functions in init
	"""
	in_function = pyclbr.readmodule_ex("npuzzle.functions")
	objet_heuristic = heuristic.Heuristic()
	objet_heuristic.set_identifiant(0)
	assert len(in_function) == len(objet_heuristic.functions)

def test_init__identifiant():
	"""
		Check if all method are in init
	"""
	objet_heuristic = heuristic.Heuristic()
	objet_heuristic.set_identifiant(0)
	for i in range(len(objet_heuristic.functions) + 1):
		exemple = heuristic.Heuristic()
		exemple.set_identifiant(i)
		assert exemple.identifiant == i

def test__get_identifiant():
	"""
		test get_identifiant
	"""
	objet_heuristic = heuristic.Heuristic()
	objet_heuristic.set_identifiant(0)
	for i in range(len(objet_heuristic.functions) + 1):
		exemple = heuristic.Heuristic()
		exemple.set_identifiant(i)
		assert exemple.get_identifiant() == i
