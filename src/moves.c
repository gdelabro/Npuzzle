#include "../npuzzle.h"

int move_possible(npuzzle *n, int *puzzle)
{
	int i;
	int ret;

	i = -1;
	ret = 0;
	while (++i < n->c)
	{
		if (!puzzle[i])
		{
			i / n->t ? ret += UP + 1 : 0;
			i / n->t != n->t - 1 ? ret += DOWN + 1 : 0;
			i % n->t ? ret += LEFT + 1 : 0;
			i % n->t != n->t - 1 ? ret += RIGHT + 1 : 0;
			return (ret);
		}
	}
	return (0);
}

int move_up(npuzzle *n, int *puzzle)
{
	int		i;
	int		j;
	int		tmp;

	i = -1;
	while (++i < n->c)
	{
		tmp = puzzle[i];
		if (!tmp && i / n->t)
		{
			puzzle[i] = puzzle[i - n->t];
			puzzle[i - n->t] = tmp;
			return (1);
		}
	}
	return (0);
}

int move_right(npuzzle *n, int *puzzle)
{
	int		i;
	int		j;
	int		tmp;

	i = -1;
	while (++i < n->c)
	{
		tmp = puzzle[i];
		if (!tmp && i % n->t != n->t - 1)
		{
			puzzle[i] = puzzle[i + 1];
			puzzle[i + 1] = tmp;
			return (1);
		}
	}
	return (0);
}

int move_down(npuzzle *n, int *puzzle)
{
	int		i;
	int		j;
	int		tmp;

	i = -1;
	while (++i < n->c)
	{
		tmp = puzzle[i];
		if (!tmp && i / n->t != n->t - 1)
		{
			puzzle[i] = puzzle[i + n->t];
			puzzle[i + n->t] = tmp;
			return (1);
		}
	}
	return (0);
}

int move_left(npuzzle *n, int *puzzle)
{
	int		i;
	int		j;
	int		tmp;

	i = -1;
	while (++i < n->c)
	{
			tmp = puzzle[i];
			if (!tmp && i % n->t)
			{
				puzzle[i] = puzzle[i - 1];
				puzzle[i - 1] = tmp;
				return (1);
			}
	}
	return (0);
}
