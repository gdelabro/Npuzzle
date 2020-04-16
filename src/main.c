#include "../npuzzle.h"

void	quit(char *str)
{
	ft_printf("%s", str);
	exit(0);
}

void	view_puzzle(npuzzle *n)
{
	int		i;
	int		j;

	i = -1;
	while (++i < n->t)
	{
		j = -1;
		while (++j < n->t)
			ft_printf("%4d", n->puzzle[i][j]);
		ft_printf("\n\n");
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
	while (i++ < n->t * n->t)
	{
		!d ? ++x : 0;
		d == 1 ? ++y : 0;
		d == 2 ? --x : 0;
		d == 3 ? --y : 0;
		n->solved[y][x] = (i != n->t * n->t) ? i : 0;
		n->random ? n->puzzle[y][x] = n->solved[y][x] : 0;
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
	int i;

	i = -1;
	n->solved = malloc(n->t * sizeof(int*));
	n->random ? n->puzzle = malloc(n->t * sizeof(int*)) : 0;
	if (!n->solved || !n->puzzle)
		exit(-1);
	while (++i < n->t)
	{
		n->solved[i] = malloc(n->t * sizeof(int));
		n->random ? n->puzzle[i] = malloc(n->t * sizeof(int)) : 0;
		if (!n->solved[i] || !n->puzzle[i])
			exit(-1);
	}
	n->c = n->t * n->t;
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
	view_puzzle(&n);
	a_star(&n);
}
