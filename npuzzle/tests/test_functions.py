"""
	docstring
"""

from npuzzle import functions

def test_manhattan__ok_1():
	"""
		test manhattan some valid anwer, with swall puzzle
	"""
	exemple = []
	for i in range(1, 2*2+1):
		exemple.append(i)
	assert functions.manhattan(
		2,
		exemple,
		exemple
	) == 0

def test_manhattan__ok_2():
	"""
		test manhattan some valid anwer, with medium puzzle
	"""
	exemple = []
	for i in range(1, 5*5+1):
		exemple.append(i)
	assert functions.manhattan(
		5,
		exemple,
		exemple
	) == 0

def test_manhattan__ok_3():
	"""
		test manhattan some valid anwer, with big puzzle
	"""
	exemple = []
	for i in range(1, 12*12+1):
		exemple.append(i)
	assert functions.manhattan(
		12,
		exemple,
		exemple
	) == 0

def test_manhattan__ko_1():
	"""
		test manhattan some unvalid anwer, with small change
	"""
	exemple = []
	for i in range(1, 3*3+1):
		exemple.append(i)
	assert functions.manhattan(
		3,
		[1, 2, 3, 5, 4, 6, 7, 8, 9],
		[1, 2, 3, 4, 5, 6, 7, 8, 9]
	) == 2

def test_manhattan__ko_2():
	"""
		test manhattan some unvalid anwer, with a far change
	"""
	exemple = []
	for i in range(1, 3*3+1):
		exemple.append(i)
	assert functions.manhattan(
		3,
		[9, 2, 3, 4, 5, 6, 7, 8, 1],
		[1, 2, 3, 4, 5, 6, 7, 8, 9]
	) == 4

def test_manhattan__ko_3():
	"""
		test manhattan some unvalid anwer, with many change
	"""
	exemple = []
	for i in range(1, 3*3+1):
		exemple.append(i)
	assert functions.manhattan(
		3,
		[4, 6, 2, 9, 8, 3, 1, 5, 7],
		[1, 2, 3, 4, 5, 6, 7, 8, 9]
	) == 11

def test_euclidian__ok_1():
	"""
		test euclidian some valid anwer, with swall puzzle
	"""
	exemple = []
	for i in range(1, 2*2+1):
		exemple.append(i)
	assert functions.euclidian(
		2,
		exemple,
		exemple
	) == 0

def test_euclidian__ok_2():
	"""
		test euclidian some valid anwer, with medium puzzle
	"""
	exemple = []
	for i in range(1, 5*5+1):
		exemple.append(i)
	assert functions.euclidian(
		5,
		exemple,
		exemple
	) == 0

def test_euclidian__ok_3():
	"""
		test euclidian some valid anwer, with big puzzle
	"""
	exemple = []
	for i in range(1, 12*12+1):
		exemple.append(i)
	assert functions.euclidian(
		12,
		exemple,
		exemple
	) == 0

def test_euclidian__ko_1():
	"""
		test euclidian some unvalid anwer, with small change
	"""
	exemple = []
	for i in range(1, 3*3+1):
		exemple.append(i)
	assert functions.euclidian(
		3,
		[1, 2, 3, 5, 4, 6, 7, 8, 9],
		[1, 2, 3, 4, 5, 6, 7, 8, 9]
	) == 2

def test_euclidian__ko_2():
	"""
		test euclidian some unvalid anwer, with a far change
	"""
	exemple = []
	for i in range(1, 3*3+1):
		exemple.append(i)
	assert functions.euclidian(
		3,
		[9, 2, 3, 4, 5, 6, 7, 8, 1],
		[1, 2, 3, 4, 5, 6, 7, 8, 9]
	) == 2.8284271247461903

def test_euclidian__ko_3():
	"""
		test euclidian some unvalid anwer, with many change
	"""
	exemple = []
	for i in range(1, 3*3+1):
		exemple.append(i)
	assert functions.euclidian(
		3,
		[4, 6, 2, 9, 8, 3, 1, 5, 7],
		[1, 2, 3, 4, 5, 6, 7, 8, 9]
	) == 10.414213562373096

def test_not_in_place__ok_1():
	"""
		test not_in_place some valid anwer, with swall puzzle
	"""
	exemple = []
	for i in range(1, 2*2+1):
		exemple.append(i)
	assert functions.not_in_place(
		2,
		exemple,
		exemple
	) == 0

def test_not_in_place__ok_2():
	"""
		test not_in_place some valid anwer, with medium puzzle
	"""
	exemple = []
	for i in range(1, 5*5+1):
		exemple.append(i)
	assert functions.not_in_place(
		5,
		exemple,
		exemple
	) == 0

def test_not_in_place__ok_3():
	"""
		test not_in_place some valid anwer, with big puzzle
	"""
	exemple = []
	for i in range(1, 12*12+1):
		exemple.append(i)
	assert functions.not_in_place(
		12,
		exemple,
		exemple
	) == 0

def test_not_in_place__ko_1():
	"""
		test not_in_place some unvalid anwer, with small change
	"""
	exemple = []
	for i in range(1, 3*3+1):
		exemple.append(i)
	assert functions.not_in_place(
		3,
		[1, 2, 3, 5, 4, 6, 7, 8, 9],
		[1, 2, 3, 4, 5, 6, 7, 8, 9]
	) == 2

def test_not_in_place__ko_2():
	"""
		test not_in_place some unvalid anwer, with a far change
	"""
	exemple = []
	for i in range(1, 3*3+1):
		exemple.append(i)
	assert functions.not_in_place(
		3,
		[9, 2, 3, 4, 5, 6, 7, 8, 1],
		[1, 2, 3, 4, 5, 6, 7, 8, 9]
	) == 1

def test_not_in_place__ko_3():
	"""
		test not_in_place some unvalid anwer, with many change
	"""
	exemple = []
	for i in range(1, 3*3+1):
		exemple.append(i)
	assert functions.not_in_place(
		3,
		[4, 6, 2, 9, 8, 3, 1, 5, 7],
		[1, 2, 3, 4, 5, 6, 7, 8, 9]
	) == 8
