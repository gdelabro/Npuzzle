#include "../npuzzle.h"

int		is_inverted(npuzzle *n, int a, int b)
{
	int i;
	int nb;

	if (!a || !b)
		return (0);
	i = -1;
	while (++i < n->c)
	{
		nb = n->solved[i / n->t][i % n->t];
		if (nb == a || nb == b)
			return (nb == b ? 1 : 0);
	}
	return (1);
}

int		check_if_solvable(npuzzle *n)
{
	int inversions;
	int puzz[n->c];
	int i, j;
	int row1, row2;

	i = -1;
	inversions = 0;
	while (++i != n->c)
		puzz[i] = n->puzzle[i / n->t][i % n->t];
	i = -1;
	while (++i != n->c)
	{
		j = i;
		while (++j < n->c)
			if (is_inverted(n, puzz[i], puzz[j]))
				inversions++;
	}
	if (n->t % 2 == 1)
		return (inversions % 2);
	i = -1;
	while (++i < n->c)
	{
		if (!n->solved[i / n->t][i % n->t])
			row1 = i / n->t;
		if (!puzz[i])
			row2 = i / n->t;
	}
	return ((inversions + row1 - row2) % 2);
}

void	invert_for_solvable(npuzzle *n)
{
	int puzz[n->c];
	int i, j;
	int tmp;

	i = -1;
	while (++i != n->c)
		puzz[i] = n->puzzle[i / n->t][i % n->t];
	i = -1;
	while (++i != n->c)
	{
		j = i;
		while (++j < n->c)
			if (puzz[i] && puzz[j])
			{
				tmp = n->puzzle[i / n->t][i % n->t];
				n->puzzle[i / n->t][i % n->t] = n->puzzle[j / n->t][j % n->t];
				n->puzzle[j / n->t][j % n->t] = tmp;
				return ;
			}
	}
}

//fisher yates
void	random_scrambler(npuzzle *n)
{
	int i, j;
	int xi, yi, xj, yj;
	int tmp;

	i = n->c - 1;
	srand(time(NULL));
	srand(rand());
	while (i > 0)
	{
		j = rand() % i;
		xi = i % n->t;
		yi = i / n->t;
		xj = j % n->t;
		yj = j / n->t;
		tmp = n->puzzle[xi][yi];
		n->puzzle[xi][yi] = n->puzzle[xj][yj];
		n->puzzle[xj][yj] = tmp;
		--i;
	}
	if (check_if_solvable(n))
		invert_for_solvable(n);
}
