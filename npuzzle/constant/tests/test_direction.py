"""
	docstring
"""

from npuzzle.constant import direction

def test_none():
	"""
		test the constant direction.NONE
	"""
	assert isinstance(direction.NONE, int)
	assert direction.NONE == 5

def test_up():
	"""
		test the constant direction.UP
	"""
	assert isinstance(direction.UP, int)
	assert direction.UP == 8

def test_down():
	"""
		test the constant direction.DOWN
	"""
	assert isinstance(direction.DOWN, int)
	assert direction.DOWN == 2

def test_right():
	"""
		test the constant direction.RIGHT
	"""
	assert isinstance(direction.RIGHT, int)
	assert direction.RIGHT == 6

def test_left():
	"""
		test the constant direction.LEFT
	"""
	assert isinstance(direction.LEFT, int)
	assert direction.LEFT == 4
