"""
	docstring
"""

import pytest

from npuzzle import node
from npuzzle import functions

def test_init__raises():
	"""
		docstring
	"""
	with pytest.raises(
		ValueError,
		match="The puzzle's size is 5, it should be 9 : 1, 2, 3, 4, 5"
	):
		node.Node(
			[3,
			[1, 2, 3, 4, 5]],
			None, 5, [0, functions.manhattan]
		)

	with pytest.raises(
		ValueError,
		match="The puzzle's size is 9, it should be 4 : 1, 2, 3, 4, 5, 6, 7, 8, 9"
	):
		node.Node(
			[2,
			[1, 2, 3, 4, 5, 6, 7, 8, 9]],
			None, 5, [0, functions.manhattan]
		)
