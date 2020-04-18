#ifndef RCS_H
# define RCS_H

#include <unistd.h>
#include <stdlib.h>
#include <time.h>
#include <sys/types.h>
#include <sys/stat.h>
#include "ft_printf/ft_printf.h"

#define UP      0b10000
#define RIGHT  0b100000
#define DOWN  0b1000000
#define LEFT 0b10000000
#define MOVE_POSSIBLE 0b1111

typedef struct		s_puzzle
{
	int		random;
	int		t;
	int		c;
	int		*solved;
	int		*puzzle;
}					npuzzle;

typedef struct		s_state_list
{
	void	*parent;
	int		*puzzle;
	int		f;
	int		g;
	int		h;
	int		move;
	int		nb_child;
	void	**child;
	void	*next;
}					state_list;

typedef struct		s_Astar
{
	state_list	*open;
	state_list	*closed;
}					t_a_star;

void	view_puzzle(npuzzle *n, int *puzzle);
void	init(npuzzle *n);
void	quit(char *str);

int		move_up(npuzzle *n, int *puzzle);
int		move_right(npuzzle *n, int *puzzle);
int		move_down(npuzzle *n, int *puzzle);
int		move_left(npuzzle *n, int *puzzle);
int		move_possible(npuzzle *n, int *puzzle);

void	random_scrambler(npuzzle *n);
int		check_if_solvable(npuzzle *n);

void	parser(npuzzle *n, char *str);
void	check_numbers(npuzzle *n);

void	a_star(npuzzle *n);

int		manhattan(npuzzle *n, int *puzzle);

state_list	*add_state_to_list(state_list *open, state_list *to_add);
state_list	*creat_state_list(npuzzle *n, int *puzzle, state_list *parent);
state_list	*creat_state_child(npuzzle *n, state_list *node);
void		calc_fgh(npuzzle *n, state_list *node);

#endif
