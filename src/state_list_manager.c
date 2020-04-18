#include "../npuzzle.h"

void		calc_fgh(npuzzle *n, state_list *node)
{
	node->g = node->parent ? ((state_list*)node->parent)->g + 1 : 0;
	node->h = manhattan(n, node->puzzle);
	node->f = node->g + node->h;
}

state_list	*creat_state_list(npuzzle *n, int *puzzle, state_list *parent)
{
	state_list *s;
	int i, j;

	if (!(s = malloc(sizeof(state_list))) || !(s->puzzle = malloc(sizeof(int*) * n->c)))
		quit("malloc failed\n");
	i = -1;
	while (++i < n->c)
		s->puzzle[i] = puzzle[i];
	s->parent = parent;
	s->child = NULL;
	s->next = NULL;
	return (s);
}

state_list	*creat_state_child(npuzzle *n, state_list *node)
{
	state_list *tmp;
	int moves;
	int i;
	int j;

	moves = move_possible(n, node->puzzle);
	node->nb_child = moves & MOVE_POSSIBLE;
	if (!(node->child = malloc(sizeof(void*) * node->nb_child)))
		quit("malloc failed\n");
	moves >>= 3;
	i = -1;
	j = -1;
	while (++i < 4)
	{
		if ((moves >>= 1) & 1)
		{
			node->child[++j] = creat_state_list(n, node->puzzle, node);
			tmp = node->child[j];
			!i ? tmp->move = UP : 0;
			i == 1 ? tmp->move = RIGHT : 0;
			i == 2 ? tmp->move = DOWN : 0;
			i == 3 ? tmp->move = LEFT : 0;
			!i ? move_up(n, tmp->puzzle) : 0;
			i == 1 ? move_right(n, tmp->puzzle) : 0;
			i == 2 ? move_down(n, tmp->puzzle) : 0;
			i == 3 ? move_left(n, tmp->puzzle) : 0;
			calc_fgh(n, node->child[j]);
		}
	}
	return (node);
}

state_list	*add_state_to_list(state_list *open, state_list *to_add)
{
	state_list *node;
	if (!open)
		return (to_add);
	node = open;
	while (node->next)
		node = node->next;
	node->next = to_add;
	return (open);
}
