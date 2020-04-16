#include "../npuzzle.h"

void	check_numbers(npuzzle *n)
{
	int i, j;
	int puzz[n->c];

	i = -1;
	while (++i != n->c)
		puzz[i] = n->puzzle[i / n->t][i % n->t];
	j = -1;
	while (++j < n->c && (i = -1))
	{
		while (++i < n->c)
			if (puzz[i] == j)
				break ;
		if (i == n->c)
			quit("bad number in puzzle\n");
	}
}

int		check_valid_line(char *line)
{
	int		i;

	i = -1;
	while (line[++i])
		if (line[i] != ' ' && (line[i] > '9' || line[i] < '0'))
			return (0);
	return (1);
}

int		parsing_puzzle(npuzzle *n, char *line, int mode)
{
	int i;
	int j;

	if (!n->puzzle)
		if (!(n->puzzle = malloc(sizeof(int*) * n->t)))
			quit("malloc failed\n");
	if (!check_valid_line(line) || ft_nbmot(line, ' ') != n->t)
		quit("bad puzzle format\n");
	if (!(n->puzzle[mode] = malloc(sizeof(int) * n->t)))
		quit("malloc failed\n");
	i = -1;
	j = -1;
	while (line[++i])
		if (line[i] != ' ' && (!i || line[i - 1] == ' '))
			n->puzzle[mode][++j] = ft_atoi(line + i);
	return (mode + 1);
}

int		parsing_size(npuzzle *n, char *line)
{
	int i;

	if (!check_valid_line(line) || ft_nbmot(line, ' ') > 1)
		quit("bad size of puzzle!\n");
	if (!ft_nbmot(line, ' '))
		return (-1);
	i = -1;
	while (line[++i] == ' ')
		;
	n->t = ft_atoi(line + i);
	return (0);
}

void	parsing_file(npuzzle *n, char *file_name)
{
	int		fd;
	char	*line;
	int		mode;
	int		i;
	struct stat st;

	mode = -1;
	n->puzzle = NULL;
	fd = open(file_name, O_RDONLY);
	if (fd <= 0 || fstat(fd, &st) != 0 || !S_ISREG(st.st_mode))
		quit("bad file name\n");
	while (get_next_line(fd, &line) == 1)
	{
		i = -1;
		if (!line)
			quit("malloc failed\n");
		while (line[++i] && line[i] != '#')
			;
		line[i] = 0;
		if (mode == -1)
			mode = parsing_size(n, line);
		else
			mode = parsing_puzzle(n, line, mode);
		if (mode > n->t)
			quit("bad size of puzzle\n");
		ft_strdel(&line);
	}
	n->c = n->t * n->t;
}

void	parser(npuzzle *n, char *str)
{
	int		i;

	n->random = str[0] == '-' ? 1 : 0;
	if (str[0] == '-')
	{
		n->t = ft_atoi(str + 1);
		if (n->t < 2)
			quit("puzzle size too small\n");
	}
	else
		parsing_file(n, str);
	init(n);
	check_numbers(n);
	if (check_if_solvable(n))
		quit("puzzle unsolvable\n");
}
