#include "../npuzzle.h"

void	quit(char *str)
{
	ft_printf("%s", str);
	exit(0);
}

void	view_puzzle(npuzzle *n, int *puzzle)
{
	int		i;
	int		j;

	i = -1;
	while (++i < n->c)
	{
		ft_printf("%4d", puzzle[i]);
		(i % n->t) == n->t - 1 ? ft_printf("\n\n") : 0;
	}
	ft_printf("\n\n\n");
}

void	create_snail(npuzzle *n)
{
	int i;
	int x, y;
	int d;
	int h;

	i = 0;
	x = -1;
	y = 0;
	d = 0;
	h = 0;
	while (i++ < n->c)
	{
		!d ? ++x : 0;
		d == 1 ? ++y : 0;
		d == 2 ? --x : 0;
		d == 3 ? --y : 0;
		n->solved[y * n->t + x] = (i != n->c) ? i : 0;
		n->random ? n->puzzle[y * n->t + x] = n->solved[y * n->t + x] : 0;
		if (!d && x == n->t - h - 1)
			d = 1;
		else if (d == 1 && y == n->t - h - 1)
			d = 2;
		else if (d == 2 && x == h)
			d = 3;
		else if (d == 3 && y == h + 1 && ++h)
			d = 0;
	}
}

void	init(npuzzle *n)
{
	n->c = n->t * n->t;
	n->solved = malloc(n->c * sizeof(int*));
	n->random ? n->puzzle = malloc(n->c * sizeof(int*)) : 0;
	if (!n->solved || !n->puzzle)
		quit("malloc failed\n");
	create_snail(n);
	n->random ? random_scrambler(n) : 0;
}

int		main(int ac, char **av)
{
	npuzzle n;

	if (ac != 2 || !av[1][0])
		quit("usage: ./npuzzle file\n            or\n       ./npuzzle -XX\n\
XX is the size of the puzzle\n");
	parser(&n, av[1]);
	view_puzzle(&n, n.puzzle);
	a_star(&n);
}
