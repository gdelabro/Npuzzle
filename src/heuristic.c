#include "../npuzzle.h"

int		manhattan(npuzzle *n, int **puzzle)
{
	int i1, j1;
	int i2, j2;
	int res;

	res = 0;
	i1 = -1;
	while (++i1 < n->t)
	{
		j1 = -1;
		while (++j1 < n->t)
		{
			i2 = -1;
			while (++i2 < n->t)
			{
				j2 = -1;
				while (++j2 < n->t)
					if (puzzle[i1][j1] == n->solved[i2][j2] && puzzle[i1][j1])
					{
						res += ABS(i1 - i2) + ABS(j1 - j2);
						i2 = n->t;
						j2 = n->t;
					}
			}
		}
	}
	return (res);
}
