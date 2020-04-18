#include "../npuzzle.h"

int		manhattan(npuzzle *n, int *puzzle)
{
	int i1;
	int i2;
	int res;

	res = 0;
	i1 = -1;
	while (++i1 < n->c)
	{
		i2 = -1;
		while (++i2 < n->c)
			if (puzzle[i1] == n->solved[i2] && puzzle[i1])
			{
				res += ABS(i1 / n->t - i2 / n->t) + ABS(i1 % n->t - i2 % n->t);
				i2 = n->c;
			}
	}
	return (res);
}
