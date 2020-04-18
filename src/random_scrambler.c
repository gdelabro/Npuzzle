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
		nb = n->solved[i];
		if (nb == a || nb == b)
			return (nb == b ? 1 : 0);
	}
	return (1);
}

int		check_if_solvable(npuzzle *n)
{
	int inversions;
	int i, j;
	int row1, row2;

	inversions = 0;

	i = -1;
	while (++i != n->c)
	{
		j = i;
		while (++j < n->c)
			if (is_inverted(n, n->puzzle[i], n->puzzle[j]))
				inversions++;
	}
	if (n->t % 2 == 1)
		return (inversions % 2);
	i = -1;
	while (++i < n->c)
	{
		if (!n->solved[i])
			row1 = i / n->t;
		if (!n->puzzle[i])
			row2 = i / n->t;
	}
	return ((inversions + row1 - row2) % 2);
}

void	invert_for_solvable(npuzzle *n)
{
	int i, j;
	int tmp;

	i = -1;
	while (++i != n->c)
	{
		j = i;
		while (++j < n->c)
			if (n->puzzle[i] && n->puzzle[j])
			{
				tmp = n->puzzle[i];
				n->puzzle[i] = n->puzzle[j];
				n->puzzle[j] = tmp;
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
		tmp = n->puzzle[xi * n->t + yi];
		n->puzzle[xi * n->t + yi] = n->puzzle[xj * n->t + yj];
		n->puzzle[xj * n->t + yj] = tmp;
		--i;
	}
	if (check_if_solvable(n))
		invert_for_solvable(n);
}
