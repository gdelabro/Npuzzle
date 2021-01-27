"""
    this file contains the snail solution of the puzzle
    in a constant.
"""

def create_solution(size: int) -> None:
	"""
		this function creates the snail solution of the puzzle
	"""
	sol = [0 for i in range(0, size ** 2)]
	i = 0
	xcol = -1
	ycol = 0
	direction = 0
	round_number = 0
	for i in range(1, size ** 2 + 1):
		if not direction:
			xcol += 1
		if direction == 1:
			ycol += 1
		if direction == 2:
			xcol -= 1
		if direction == 3:
			ycol -= 1
		if not i == size ** 2:
			sol[ycol * size + xcol] = i
		else:
			sol[ycol * size + xcol] = 0
		if direction == 0 and xcol == size - round_number - 1:
			direction = 1
		if direction == 1 and ycol == size - round_number - 1:
			direction = 2
		if direction == 2 and xcol == round_number:
			direction = 3
		if direction == 3 and ycol == round_number + 1:
			direction,round_number = 0,round_number+1
	return sol

solution = []

if __name__ == "__main__":
	solution = create_solution(3)
	print(solution)
