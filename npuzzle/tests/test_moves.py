"""
	docstring
"""

from npuzzle import moves

def test_move_up__ok_3():
	"""
		test if move up work proprely with size 3
	"""
	old_puzzle = [
		1, 2, 3,
		0, 5, 6,
		7, 8, 9
	]
	obj_puzzle = [
		0, 2, 3,
		1, 5, 6,
		7, 8, 9
	]
	new_puzzle = moves.move_up(3, old_puzzle)
	assert new_puzzle == obj_puzzle
	old_puzzle = [
		1, 2, 3,
		4, 0, 6,
		7, 8, 9
	]
	obj_puzzle = [
		1, 0, 3,
		4, 2, 6,
		7, 8, 9
	]
	new_puzzle = moves.move_up(3, old_puzzle)
	assert new_puzzle == obj_puzzle
	old_puzzle = [
		1, 2, 3,
		4, 5, 0,
		7, 8, 9
	]
	obj_puzzle = [
		1, 2, 0,
		4, 5, 3,
		7, 8, 9
	]
	new_puzzle = moves.move_up(3, old_puzzle)
	assert new_puzzle == obj_puzzle
	old_puzzle = [
		1, 2, 3,
		4, 5, 6,
		0, 8, 9
	]
	obj_puzzle = [
		1, 2, 3,
		0, 5, 6,
		4, 8, 9
	]
	new_puzzle = moves.move_up(3, old_puzzle)
	assert new_puzzle == obj_puzzle
	old_puzzle = [
		1, 2, 3,
		4, 5, 6,
		7, 0, 9
	]
	obj_puzzle = [
		1, 2, 3,
		4, 0, 6,
		7, 5, 9
	]
	new_puzzle = moves.move_up(3, old_puzzle)
	assert new_puzzle == obj_puzzle
	old_puzzle = [
		1, 2, 3,
		4, 5, 6,
		7, 8, 0
	]
	obj_puzzle = [
		1, 2, 3,
		4, 5, 0,
		7, 8, 6
	]
	new_puzzle = moves.move_up(3, old_puzzle)
	assert new_puzzle == obj_puzzle

def test_move_up__ok_4plus():
	"""
		test if move up work proprely with size 4 or plus
	"""
	old_puzzle = [
		1,	2,	3,	4,
		5,	6,	7,	8,
		9,	10,	11,	12,
		13,	0,	15,	16
	]
	obj_puzzle = [
		1,	2,	3,	4,
		5,	6,	7,	8,
		9,	0,	11,	12,
		13,	10,	15,	16
	]
	new_puzzle = moves.move_up(4, old_puzzle)
	assert new_puzzle == obj_puzzle
	old_puzzle = [
		1,	2,	3,	4,
		0,	6,	7,	8,
		9,	10,	11,	12,
		13,	14,	15,	16
	]
	obj_puzzle = [
		0,	2,	3,	4,
		1,	6,	7,	8,
		9,	10,	11,	12,
		13,	14,	15,	16
	]
	new_puzzle = moves.move_up(4, old_puzzle)
	assert new_puzzle == obj_puzzle
	old_puzzle = [
		1,	2,	3,	4,	5,	6,	7,	8,	9,	10,
		11,	12,	13,	14,	15,	16,	17,	18,	19,	20,
		21,	22,	23,	24,	25,	26,	0,	28,	29,	30,
		31,	32,	33,	34,	35,	36,	37,	38,	39,	40,
		41,	42,	43,	44,	45,	46,	47,	48,	49,	50,
		51,	52,	53,	54,	55,	56,	57,	58,	59,	60,
		61,	62,	63,	64,	65,	66,	67,	68,	69,	70,
		71,	72,	73,	74,	75,	76,	77,	78,	79,	80,
		81,	82,	83,	84,	85,	86,	87,	88,	89,	90,
		91,	92,	93,	94,	95,	96,	97,	98,	99,	100
	]
	obj_puzzle = [
		1,	2,	3,	4,	5,	6,	7,	8,	9,	10,
		11,	12,	13,	14,	15,	16,	0,	18,	19,	20,
		21,	22,	23,	24,	25,	26,	17,	28,	29,	30,
		31,	32,	33,	34,	35,	36,	37,	38,	39,	40,
		41,	42,	43,	44,	45,	46,	47,	48,	49,	50,
		51,	52,	53,	54,	55,	56,	57,	58,	59,	60,
		61,	62,	63,	64,	65,	66,	67,	68,	69,	70,
		71,	72,	73,	74,	75,	76,	77,	78,	79,	80,
		81,	82,	83,	84,	85,	86,	87,	88,	89,	90,
		91,	92,	93,	94,	95,	96,	97,	98,	99,	100
	]
	new_puzzle = moves.move_up(10, old_puzzle)
	assert new_puzzle == obj_puzzle

def test_move_up__ko_3():
	"""
		test if move up work proprely when 0 is on the top border with size 3
	"""
	old_puzzle = [
		0, 2, 3,
		4, 5, 6,
		7, 8, 9
	]
	new_puzzle = moves.move_up(3, old_puzzle)
	assert new_puzzle is None
	old_puzzle = [
		1, 0, 3,
		4, 5, 6,
		7, 8, 9
	]
	new_puzzle = moves.move_up(3, old_puzzle)
	assert new_puzzle is None
	old_puzzle = [
		1, 2, 0,
		4, 5, 6,
		7, 8, 9
	]
	new_puzzle = moves.move_up(3, old_puzzle)
	assert new_puzzle is None

def test_move_up__ko_4plus():
	"""
		test if move up work proprely when 0 is on the top border with size 3
	"""
	old_puzzle = [
		0,	2,	3,	4,
		5,	6,	7,	8,
		9,	10,	11,	12,
		13,	14,	15,	16
	]
	new_puzzle = moves.move_up(4, old_puzzle)
	assert new_puzzle is None
	old_puzzle = [
		1,	0,	3,	4,
		5,	6,	7,	8,
		9,	10,	11,	12,
		13,	14,	15,	16
	]
	new_puzzle = moves.move_up(4, old_puzzle)
	assert new_puzzle is None
	old_puzzle = [
		1,	2,	0,	4,
		5,	6,	7,	8,
		9,	10,	11,	12,
		13,	14,	15,	16
	]
	new_puzzle = moves.move_up(4, old_puzzle)
	assert new_puzzle is None
	old_puzzle = [
		1,	2,	3,	0,
		5,	6,	7,	8,
		9,	10,	11,	12,
		13,	14,	15,	16
	]
	new_puzzle = moves.move_up(4, old_puzzle)
	assert new_puzzle is None
	old_puzzle = [
		1,	2,	3,	4,	5,	6,	0,	8,	9,	10,
		11,	12,	13,	14,	15,	16,	17,	18,	19,	20,
		21,	22,	23,	24,	25,	26,	27,	28,	29,	30,
		31,	32,	33,	34,	35,	36,	37,	38,	39,	40,
		41,	42,	43,	44,	45,	46,	47,	48,	49,	50,
		51,	52,	53,	54,	55,	56,	57,	58,	59,	60,
		61,	62,	63,	64,	65,	66,	67,	68,	69,	70,
		71,	72,	73,	74,	75,	76,	77,	78,	79,	80,
		81,	82,	83,	84,	85,	86,	87,	88,	89,	90,
		91,	92,	93,	94,	95,	96,	97,	98,	99,	100
	]
	new_puzzle = moves.move_up(10, old_puzzle)
	assert new_puzzle is None
	old_puzzle = [
		1,	2,	3,	4,	5,	6,	7,	8,	9,	0,
		11,	12,	13,	14,	15,	16,	17,	18,	19,	20,
		21,	22,	23,	24,	25,	26,	27,	28,	29,	30,
		31,	32,	33,	34,	35,	36,	37,	38,	39,	40,
		41,	42,	43,	44,	45,	46,	47,	48,	49,	50,
		51,	52,	53,	54,	55,	56,	57,	58,	59,	60,
		61,	62,	63,	64,	65,	66,	67,	68,	69,	70,
		71,	72,	73,	74,	75,	76,	77,	78,	79,	80,
		81,	82,	83,	84,	85,	86,	87,	88,	89,	90,
		91,	92,	93,	94,	95,	96,	97,	98,	99,	100
	]
	new_puzzle = moves.move_up(10, old_puzzle)
	assert new_puzzle is None

def test_move_down__ok_3():
	"""
		test if move down work proprely with size 3
	"""
	old_puzzle = [
		0, 2, 3,
		4, 5, 6,
		7, 8, 9
	]
	obj_puzzle = [
		4, 2, 3,
		0, 5, 6,
		7, 8, 9
	]
	new_puzzle = moves.move_down(3, old_puzzle)
	assert new_puzzle == obj_puzzle
	old_puzzle = [
		1, 0, 3,
		4, 5, 6,
		7, 8, 9
	]
	obj_puzzle = [
		1, 5, 3,
		4, 0, 6,
		7, 8, 9
	]
	new_puzzle = moves.move_down(3, old_puzzle)
	assert new_puzzle == obj_puzzle
	old_puzzle = [
		1, 2, 0,
		4, 5, 6,
		7, 8, 9
	]
	obj_puzzle = [
		1, 2, 6,
		4, 5, 0,
		7, 8, 9
	]
	new_puzzle = moves.move_down(3, old_puzzle)
	assert new_puzzle == obj_puzzle
	old_puzzle = [
		1, 2, 3,
		0, 5, 6,
		7, 8, 9
	]
	obj_puzzle = [
		1, 2, 3,
		7, 5, 6,
		0, 8, 9
	]
	new_puzzle = moves.move_down(3, old_puzzle)
	assert new_puzzle == obj_puzzle
	old_puzzle = [
		1, 2, 3,
		4, 0, 6,
		7, 8, 9
	]
	obj_puzzle = [
		1, 2, 3,
		4, 8, 6,
		7, 0, 9
	]
	new_puzzle = moves.move_down(3, old_puzzle)
	assert new_puzzle == obj_puzzle
	old_puzzle = [
		1, 2, 3,
		4, 5, 0,
		7, 8, 9
	]
	obj_puzzle = [
		1, 2, 3,
		4, 5, 9,
		7, 8, 0
	]
	new_puzzle = moves.move_down(3, old_puzzle)
	assert new_puzzle == obj_puzzle

def test_move_down__ok_4plus():
	"""
		test if move down work proprely with size 4 or plus
	"""
	old_puzzle = [
		1,	2,	3,	4,
		5,	6,	0,	8,
		9,	10,	11,	12,
		13,	14,	15,	16
	]
	obj_puzzle = [
		1,	2,	3,	4,
		5,	6,	11,	8,
		9,	10,	0,	12,
		13,	14,	15,	16
	]
	new_puzzle = moves.move_down(4, old_puzzle)
	assert new_puzzle == obj_puzzle
	old_puzzle = [
		1,	2,	3,	4,
		0,	6,	7,	8,
		9,	10,	11,	12,
		13,	14,	15,	16
	]
	obj_puzzle = [
		1,	2,	3,	4,
		9,	6,	7,	8,
		0,	10,	11,	12,
		13,	14,	15,	16
	]
	new_puzzle = moves.move_down(4, old_puzzle)
	assert new_puzzle == obj_puzzle
	old_puzzle = [
		1,	2,	3,	4,	5,	6,	7,	8,	9,	10,
		11,	12,	13,	14,	15,	16,	17,	18,	19,	20,
		21,	22,	23,	24,	25,	26,	0,	28,	29,	30,
		31,	32,	33,	34,	35,	36,	37,	38,	39,	40,
		41,	42,	43,	44,	45,	46,	47,	48,	49,	50,
		51,	52,	53,	54,	55,	56,	57,	58,	59,	60,
		61,	62,	63,	64,	65,	66,	67,	68,	69,	70,
		71,	72,	73,	74,	75,	76,	77,	78,	79,	80,
		81,	82,	83,	84,	85,	86,	87,	88,	89,	90,
		91,	92,	93,	94,	95,	96,	97,	98,	99,	100
	]
	obj_puzzle = [
		1,	2,	3,	4,	5,	6,	7,	8,	9,	10,
		11,	12,	13,	14,	15,	16,	17,	18,	19,	20,
		21,	22,	23,	24,	25,	26,	37,	28,	29,	30,
		31,	32,	33,	34,	35,	36,	0,	38,	39,	40,
		41,	42,	43,	44,	45,	46,	47,	48,	49,	50,
		51,	52,	53,	54,	55,	56,	57,	58,	59,	60,
		61,	62,	63,	64,	65,	66,	67,	68,	69,	70,
		71,	72,	73,	74,	75,	76,	77,	78,	79,	80,
		81,	82,	83,	84,	85,	86,	87,	88,	89,	90,
		91,	92,	93,	94,	95,	96,	97,	98,	99,	100
	]
	new_puzzle = moves.move_down(10, old_puzzle)
	assert new_puzzle == obj_puzzle

def test_move_down__ko_3():
	"""
		test if move down work proprely when 0 is on the top border with size 3
	"""
	old_puzzle = [
		1, 2, 3,
		4, 5, 6,
		0, 8, 9
	]
	new_puzzle = moves.move_down(3, old_puzzle)
	assert new_puzzle is None
	old_puzzle = [
		1, 2, 3,
		4, 5, 6,
		7, 0, 9
	]
	new_puzzle = moves.move_down(3, old_puzzle)
	assert new_puzzle is None
	old_puzzle = [
		1, 2, 3,
		4, 5, 6,
		7, 8, 0
	]
	new_puzzle = moves.move_down(3, old_puzzle)
	assert new_puzzle is None

def test_move_down__ko_4plus():
	"""
		test if move down work proprely when 0 is on the top border with size 3
	"""
	old_puzzle = [
		1,	2,	3,	4,
		5,	6,	7,	8,
		9,	10,	11,	12,
		0,	14,	15,	16
	]
	new_puzzle = moves.move_down(4, old_puzzle)
	assert new_puzzle is None
	old_puzzle = [
		1,	2,	3,	4,
		5,	6,	7,	8,
		9,	10,	11,	12,
		13,	0,	15,	16
	]
	new_puzzle = moves.move_down(4, old_puzzle)
	assert new_puzzle is None
	old_puzzle = [
		1,	2,	3,	4,
		5,	6,	7,	8,
		9,	10,	11,	12,
		13,	14,	0,	16
	]
	new_puzzle = moves.move_down(4, old_puzzle)
	assert new_puzzle is None
	old_puzzle = [
		1,	2,	3,	4,
		5,	6,	7,	8,
		9,	10,	11,	12,
		13,	14,	15,	0
	]
	new_puzzle = moves.move_down(4, old_puzzle)
	assert new_puzzle is None
	old_puzzle = [
		1,	2,	3,	4,	5,	6,	7,	8,	9,	10,
		11,	12,	13,	14,	15,	16,	17,	18,	19,	20,
		21,	22,	23,	24,	25,	26,	27,	28,	29,	30,
		31,	32,	33,	34,	35,	36,	37,	38,	39,	40,
		41,	42,	43,	44,	45,	46,	47,	48,	49,	50,
		51,	52,	53,	54,	55,	56,	57,	58,	59,	60,
		61,	62,	63,	64,	65,	66,	67,	68,	69,	70,
		71,	72,	73,	74,	75,	76,	77,	78,	79,	80,
		81,	82,	83,	84,	85,	86,	87,	88,	89,	90,
		91,	92,	93,	94,	95,	96,	97,	0,	99,	100
	]
	new_puzzle = moves.move_down(10, old_puzzle)
	assert new_puzzle is None
	old_puzzle = [
		1,	2,	3,	4,	5,	6,	7,	8,	9,	10,
		11,	12,	13,	14,	15,	16,	17,	18,	19,	20,
		21,	22,	23,	24,	25,	26,	27,	28,	29,	30,
		31,	32,	33,	34,	35,	36,	37,	38,	39,	40,
		41,	42,	43,	44,	45,	46,	47,	48,	49,	50,
		51,	52,	53,	54,	55,	56,	57,	58,	59,	60,
		61,	62,	63,	64,	65,	66,	67,	68,	69,	70,
		71,	72,	73,	74,	75,	76,	77,	78,	79,	80,
		81,	82,	83,	84,	85,	86,	87,	88,	89,	90,
		91,	92,	93,	94,	95,	0,	97,	98,	99,	100
	]
	new_puzzle = moves.move_down(10, old_puzzle)
	assert new_puzzle is None

def test_move_left__ok_3():
	"""
		test if move left work proprely with size 3
	"""
	old_puzzle = [
		1, 0, 3,
		4, 5, 6,
		7, 8, 9
	]
	obj_puzzle = [
		0, 1, 3,
		4, 5, 6,
		7, 8, 9
	]
	new_puzzle = moves.move_left(3, old_puzzle)
	assert new_puzzle == obj_puzzle
	old_puzzle = [
		1, 2, 0,
		4, 5, 6,
		7, 8, 9
	]
	obj_puzzle = [
		1, 0, 2,
		4, 5, 6,
		7, 8, 9
	]
	new_puzzle = moves.move_left(3, old_puzzle)
	assert new_puzzle == obj_puzzle
	old_puzzle = [
		1, 2, 3,
		4, 0, 6,
		7, 8, 9
	]
	obj_puzzle = [
		1, 2, 3,
		0, 4, 6,
		7, 8, 9
	]
	new_puzzle = moves.move_left(3, old_puzzle)
	assert new_puzzle == obj_puzzle
	old_puzzle = [
		1, 2, 3,
		4, 5, 0,
		7, 8, 9
	]
	obj_puzzle = [
		1, 2, 3,
		4, 0, 5,
		7, 8, 9
	]
	new_puzzle = moves.move_left(3, old_puzzle)
	assert new_puzzle == obj_puzzle
	old_puzzle = [
		1, 2, 3,
		4, 5, 6,
		7, 0, 9
	]
	obj_puzzle = [
		1, 2, 3,
		4, 5, 6,
		0, 7, 9
	]
	new_puzzle = moves.move_left(3, old_puzzle)
	assert new_puzzle == obj_puzzle
	old_puzzle = [
		1, 2, 3,
		4, 5, 6,
		7, 8, 0
	]
	obj_puzzle = [
		1, 2, 3,
		4, 5, 6,
		7, 0, 8
	]
	new_puzzle = moves.move_left(3, old_puzzle)
	assert new_puzzle == obj_puzzle

def test_move_left__ok_4plus():
	"""
		test if move left work proprely with size 4 or plus
	"""
	old_puzzle = [
		1,	2,	3,	4,
		5,	6,	7,	8,
		9,	10,	11,	12,
		13,	0,	15,	16
	]
	obj_puzzle = [
		1,	2,	3,	4,
		5,	6,	7,	8,
		9,	10,	11,	12,
		0,	13,	15,	16
	]
	new_puzzle = moves.move_left(4, old_puzzle)
	assert new_puzzle == obj_puzzle
	old_puzzle = [
		1,	2,	3,	4,
		5,	6,	0,	8,
		9,	10,	11,	12,
		13,	14,	15,	16
	]
	obj_puzzle = [
		1,	2,	3,	4,
		5,	0,	6,	8,
		9,	10,	11,	12,
		13,	14,	15,	16
	]
	new_puzzle = moves.move_left(4, old_puzzle)
	assert new_puzzle == obj_puzzle
	old_puzzle = [
		1,	2,	3,	4,	5,	6,	7,	8,	9,	10,
		11,	12,	13,	14,	15,	16,	17,	18,	19,	20,
		21,	22,	23,	24,	25,	26,	0,	28,	29,	30,
		31,	32,	33,	34,	35,	36,	37,	38,	39,	40,
		41,	42,	43,	44,	45,	46,	47,	48,	49,	50,
		51,	52,	53,	54,	55,	56,	57,	58,	59,	60,
		61,	62,	63,	64,	65,	66,	67,	68,	69,	70,
		71,	72,	73,	74,	75,	76,	77,	78,	79,	80,
		81,	82,	83,	84,	85,	86,	87,	88,	89,	90,
		91,	92,	93,	94,	95,	96,	97,	98,	99,	100
	]
	obj_puzzle = [
		1,	2,	3,	4,	5,	6,	7,	8,	9,	10,
		11,	12,	13,	14,	15,	16,	17,	18,	19,	20,
		21,	22,	23,	24,	25,	0,	26,	28,	29,	30,
		31,	32,	33,	34,	35,	36,	37,	38,	39,	40,
		41,	42,	43,	44,	45,	46,	47,	48,	49,	50,
		51,	52,	53,	54,	55,	56,	57,	58,	59,	60,
		61,	62,	63,	64,	65,	66,	67,	68,	69,	70,
		71,	72,	73,	74,	75,	76,	77,	78,	79,	80,
		81,	82,	83,	84,	85,	86,	87,	88,	89,	90,
		91,	92,	93,	94,	95,	96,	97,	98,	99,	100
	]
	new_puzzle = moves.move_left(10, old_puzzle)
	assert new_puzzle == obj_puzzle

def test_move_left__ko_3():
	"""
		test if move left work proprely when 0 is on the top border with size 3
	"""
	old_puzzle = [
		0, 2, 3,
		4, 5, 6,
		7, 8, 9
	]
	new_puzzle = moves.move_left(3, old_puzzle)
	assert new_puzzle is None
	old_puzzle = [
		1, 2, 3,
		0, 5, 6,
		7, 8, 9
	]
	new_puzzle = moves.move_left(3, old_puzzle)
	assert new_puzzle is None
	old_puzzle = [
		1, 2, 3,
		4, 5, 6,
		0, 8, 9
	]
	new_puzzle = moves.move_left(3, old_puzzle)
	assert new_puzzle is None

def test_move_left__ko_4plus():
	"""
		test if move left work proprely when 0 is on the top border with size 3
	"""
	old_puzzle = [
		0,	2,	3,	4,
		5,	6,	7,	8,
		9,	10,	11,	12,
		13,	14,	15,	16
	]
	new_puzzle = moves.move_left(4, old_puzzle)
	assert new_puzzle is None
	old_puzzle = [
		1,	2,	3,	4,
		0,	6,	7,	8,
		9,	10,	11,	12,
		13,	14,	15,	16
	]
	new_puzzle = moves.move_left(4, old_puzzle)
	assert new_puzzle is None
	old_puzzle = [
		1,	2,	3,	4,
		5,	6,	7,	8,
		0,	10,	11,	12,
		13,	14,	15,	16
	]
	new_puzzle = moves.move_left(4, old_puzzle)
	assert new_puzzle is None
	old_puzzle = [
		1,	2,	3,	4,
		5,	6,	7,	8,
		9,	10,	11,	12,
		0,	14,	15,	16
	]
	new_puzzle = moves.move_left(4, old_puzzle)
	assert new_puzzle is None
	old_puzzle = [
		1,	2,	3,	4,	5,	6,	7,	8,	9,	10,
		11,	12,	13,	14,	15,	16,	17,	18,	19,	20,
		0,	22,	23,	24,	25,	26,	27,	28,	29,	30,
		31,	32,	33,	34,	35,	36,	37,	38,	39,	40,
		41,	42,	43,	44,	45,	46,	47,	48,	49,	50,
		51,	52,	53,	54,	55,	56,	57,	58,	59,	60,
		61,	62,	63,	64,	65,	66,	67,	68,	69,	70,
		71,	72,	73,	74,	75,	76,	77,	78,	79,	80,
		81,	82,	83,	84,	85,	86,	87,	88,	89,	90,
		91,	92,	93,	94,	95,	96,	97,	98,	99,	100
	]
	new_puzzle = moves.move_left(10, old_puzzle)
	assert new_puzzle is None
	old_puzzle = [
		1,	2,	3,	4,	5,	6,	7,	8,	9,	10,
		11,	12,	13,	14,	15,	16,	17,	18,	19,	20,
		21,	22,	23,	24,	25,	26,	27,	28,	29,	30,
		31,	32,	33,	34,	35,	36,	37,	38,	39,	40,
		41,	42,	43,	44,	45,	46,	47,	48,	49,	50,
		51,	52,	53,	54,	55,	56,	57,	58,	59,	60,
		61,	62,	63,	64,	65,	66,	67,	68,	69,	70,
		0,	72,	73,	74,	75,	76,	77,	78,	79,	80,
		81,	82,	83,	84,	85,	86,	87,	88,	89,	90,
		91,	92,	93,	94,	95,	96,	97,	98,	99,	100
	]
	new_puzzle = moves.move_left(10, old_puzzle)
	assert new_puzzle is None

def test_move_right__ok_3():
	"""
		test if move right work proprely with size 3
	"""
	old_puzzle = [
		0, 2, 3,
		4, 5, 6,
		7, 8, 9
	]
	obj_puzzle = [
		2, 0, 3,
		4, 5, 6,
		7, 8, 9
	]
	new_puzzle = moves.move_right(3, old_puzzle)
	assert new_puzzle == obj_puzzle
	old_puzzle = [
		1, 0, 3,
		4, 5, 6,
		7, 8, 9
	]
	obj_puzzle = [
		1, 3, 0,
		4, 5, 6,
		7, 8, 9
	]
	new_puzzle = moves.move_right(3, old_puzzle)
	assert new_puzzle == obj_puzzle
	old_puzzle = [
		1, 2, 3,
		0, 5, 6,
		7, 8, 9
	]
	obj_puzzle = [
		1, 2, 3,
		5, 0, 6,
		7, 8, 9
	]
	new_puzzle = moves.move_right(3, old_puzzle)
	assert new_puzzle == obj_puzzle
	old_puzzle = [
		1, 2, 3,
		4, 0, 6,
		7, 8, 9
	]
	obj_puzzle = [
		1, 2, 3,
		4, 6, 0,
		7, 8, 9
	]
	new_puzzle = moves.move_right(3, old_puzzle)
	assert new_puzzle == obj_puzzle
	old_puzzle = [
		1, 2, 3,
		4, 5, 6,
		0, 8, 9
	]
	obj_puzzle = [
		1, 2, 3,
		4, 5, 6,
		8, 0, 9
	]
	new_puzzle = moves.move_right(3, old_puzzle)
	assert new_puzzle == obj_puzzle
	old_puzzle = [
		1, 2, 3,
		4, 5, 6,
		7, 0, 9
	]
	obj_puzzle = [
		1, 2, 3,
		4, 5, 6,
		7, 9, 0
	]
	new_puzzle = moves.move_right(3, old_puzzle)
	assert new_puzzle == obj_puzzle

def test_move_right__ok_4plus():
	"""
		test if move right work proprely with size 4 or plus
	"""
	old_puzzle = [
		1,	2,	3,	4,
		5,	6,	7,	8,
		9,	10,	11,	12,
		0,	14,	15,	16
	]
	obj_puzzle = [
		1,	2,	3,	4,
		5,	6,	7,	8,
		9,	10,	11,	12,
		14,	0,	15,	16
	]
	new_puzzle = moves.move_right(4, old_puzzle)
	assert new_puzzle == obj_puzzle
	old_puzzle = [
		1,	2,	0,	4,
		5,	6,	7,	8,
		9,	10,	11,	12,
		13,	14,	15,	16
	]
	obj_puzzle = [
		1,	2,	4,	0,
		5,	6,	7,	8,
		9,	10,	11,	12,
		13,	14,	15,	16
	]
	new_puzzle = moves.move_right(4, old_puzzle)
	assert new_puzzle == obj_puzzle
	old_puzzle = [
		1,	2,	3,	4,	5,	6,	7,	8,	9,	10,
		11,	12,	13,	14,	15,	16,	17,	18,	19,	20,
		21,	22,	23,	24,	25,	26,	27,	28,	29,	30,
		31,	32,	33,	34,	35,	36,	37,	38,	39,	40,
		41,	42,	43,	44,	45,	46,	47,	48,	49,	50,
		51,	52,	53,	54,	55,	56,	57,	58,	59,	60,
		61,	62,	63,	64,	0,	66,	67,	68,	69,	70,
		71,	72,	73,	74,	75,	76,	77,	78,	79,	80,
		81,	82,	83,	84,	85,	86,	87,	88,	89,	90,
		91,	92,	93,	94,	95,	96,	97,	98,	99,	100
	]
	obj_puzzle = [
		1,	2,	3,	4,	5,	6,	7,	8,	9,	10,
		11,	12,	13,	14,	15,	16,	17,	18,	19,	20,
		21,	22,	23,	24,	25,	26,	27,	28,	29,	30,
		31,	32,	33,	34,	35,	36,	37,	38,	39,	40,
		41,	42,	43,	44,	45,	46,	47,	48,	49,	50,
		51,	52,	53,	54,	55,	56,	57,	58,	59,	60,
		61,	62,	63,	64,	66,	0,	67,	68,	69,	70,
		71,	72,	73,	74,	75,	76,	77,	78,	79,	80,
		81,	82,	83,	84,	85,	86,	87,	88,	89,	90,
		91,	92,	93,	94,	95,	96,	97,	98,	99,	100
	]
	new_puzzle = moves.move_right(10, old_puzzle)
	assert new_puzzle == obj_puzzle

def test_move_right__ko_3():
	"""
		test if move right work proprely when 0 is on the top border with size 3
	"""
	old_puzzle = [
		1, 2, 0,
		4, 5, 6,
		7, 8, 9
	]
	new_puzzle = moves.move_right(3, old_puzzle)
	assert new_puzzle is None
	old_puzzle = [
		1, 2, 3,
		4, 5, 0,
		7, 8, 9
	]
	new_puzzle = moves.move_right(3, old_puzzle)
	assert new_puzzle is None
	old_puzzle = [
		1, 2, 3,
		4, 5, 6,
		7, 8, 0
	]
	new_puzzle = moves.move_right(3, old_puzzle)
	assert new_puzzle is None

def test_move_right__ko_4plus():
	"""
		test if move right work proprely when 0 is on the top border with size 3
	"""
	old_puzzle = [
		1,	2,	3,	0,
		5,	6,	7,	8,
		9,	10,	11,	12,
		13,	14,	15,	16
	]
	new_puzzle = moves.move_right(4, old_puzzle)
	assert new_puzzle is None
	old_puzzle = [
		1,	2,	3,	4,
		5,	6,	7,	0,
		9,	10,	11,	12,
		13,	14,	15,	16
	]
	new_puzzle = moves.move_right(4, old_puzzle)
	assert new_puzzle is None
	old_puzzle = [
		1,	2,	3,	4,
		5,	6,	7,	8,
		9,	10,	11,	0,
		13,	14,	15,	16
	]
	new_puzzle = moves.move_right(4, old_puzzle)
	assert new_puzzle is None
	old_puzzle = [
		1,	2,	3,	4,
		5,	6,	7,	8,
		9,	10,	11,	12,
		13,	14,	15,	0
	]
	new_puzzle = moves.move_right(4, old_puzzle)
	assert new_puzzle is None
	old_puzzle = [
		1,	2,	3,	4,	5,	6,	7,	8,	9,	10,
		11,	12,	13,	14,	15,	16,	17,	18,	19,	20,
		21,	22,	23,	24,	25,	26,	27,	28,	29,	30,
		31,	32,	33,	34,	35,	36,	37,	38,	39,	40,
		41,	42,	43,	44,	45,	46,	47,	48,	49,	50,
		51,	52,	53,	54,	55,	56,	57,	58,	59,	60,
		61,	62,	63,	64,	65,	66,	67,	68,	69,	70,
		71,	72,	73,	74,	75,	76,	77,	78,	79,	0,
		81,	82,	83,	84,	85,	86,	87,	88,	89,	90,
		91,	92,	93,	94,	95,	96,	97,	98,	99,	100
	]
	new_puzzle = moves.move_right(10, old_puzzle)
	assert new_puzzle is None
	old_puzzle = [
		1,	2,	3,	4,	5,	6,	7,	8,	9,	0,
		11,	12,	13,	14,	15,	16,	17,	18,	19,	20,
		21,	22,	23,	24,	25,	26,	27,	28,	29,	30,
		31,	32,	33,	34,	35,	36,	37,	38,	39,	40,
		41,	42,	43,	44,	45,	46,	47,	48,	49,	50,
		51,	52,	53,	54,	55,	56,	57,	58,	59,	60,
		61,	62,	63,	64,	65,	66,	67,	68,	69,	70,
		71,	72,	73,	74,	75,	76,	77,	78,	79,	80,
		81,	82,	83,	84,	85,	86,	87,	88,	89,	90,
		91,	92,	93,	94,	95,	96,	97,	98,	99,	100
	]
	new_puzzle = moves.move_right(10, old_puzzle)
	assert new_puzzle is None
