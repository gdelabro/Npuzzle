#include "../npuzzle.h"

int move_possible(npuzzle *n, int **puzzle)
{
	int i, j;
	int ret;

	i = -1;
	ret = 0;
	while (++i < n->t)
	{
		j = -1;
		while (++j < n->t)
		{
			if (!puzzle[i][j])
			{
				i ? ret += UP + 1 : 0;
				i != n->t - 1 ? ret += DOWN + 1 : 0;
				j ? ret += LEFT + 1 : 0;
				j != n->t - 1 ? ret += RIGHT + 1 : 0;
				return (ret);
			}
		}
	}
	return (0);
}

int move_up(npuzzle *n, int **puzzle)
{
	int		i;
	int		j;
	int		tmp;

	i = -1;
	while (++i < n->t)
	{
		j = -1;
		while (++j < n->t)
		{
			tmp = puzzle[i][j];
			if (!tmp && i)
			{
				puzzle[i][j] = puzzle[i - 1][j];
				puzzle[i - 1][j] = tmp;
				return (1);
			}
			if (!tmp)
				return (0);
		}
	}
}

int move_right(npuzzle *n, int **puzzle)
{
	int		i;
	int		j;
	int		tmp;

	i = -1;
	while (++i < n->t)
	{
		j = -1;
		while (++j < n->t)
		{
			tmp = puzzle[i][j];
			if (!tmp && j != n->t - 1)
			{
				puzzle[i][j] = puzzle[i][j + 1];
				puzzle[i][j + 1] = tmp;
				return (1);
			}
			if (!tmp)
				return (0);
		}
	}
}

int move_down(npuzzle *n, int **puzzle)
{
	int		i;
	int		j;
	int		tmp;

	i = -1;
	while (++i < n->t)
	{
		j = -1;
		while (++j < n->t)
		{
			tmp = puzzle[i][j];
			if (!tmp && i != n->t - 1)
			{
				puzzle[i][j] = puzzle[i + 1][j];
				puzzle[i + 1][j] = tmp;
				return (1);
			}
			if (!tmp)
				return (0);
		}
	}
}

int move_left(npuzzle *n, int **puzzle)
{
	int		i;
	int		j;
	int		tmp;

	i = -1;
	while (++i < n->t)
	{
		j = -1;
		while (++j < n->t)
		{
			tmp = puzzle[i][j];
			if (!tmp && j)
			{
				puzzle[i][j] = puzzle[i][j - 1];
				puzzle[i][j - 1] = tmp;
				return (1);
			}
			if (!tmp)
				return (0);
		}
	}
}
