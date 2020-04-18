#include "../npuzzle.h"

void	aff_struct(state_list *list)
{
	while (list)
	{
		ft_printf("{f: %d}%s", list->f, list->next ? " -> " : "\n");
		list = list->next;
	}
}

void	sort_by_f(t_a_star *a)
{
	state_list *s;
	state_list *tmp;
	state_list *old;

	s = a->open;
	old = NULL;
	while (s && s->next)
	{
		if (s->f > ((state_list*)s->next)->f)
		{
			tmp = ((state_list*)s->next)->next;
			if (!old)
			{
				a->open = s->next;
				a->open->next = s;
			}
			else
			{
				old->next = s->next;
				((state_list*)s->next)->next = s;
			}
			s->next = tmp;
			s = a->open;
			old = NULL;
		}
		else
		{
			old = s;
			s = s->next;
		}
	}
}

int		state_is_in_closed(npuzzle *n, t_a_star *a, state_list *node)
{
	int			i;
	state_list	*closed;

	closed = a->closed;
	while (closed)
	{
		i = -1;
		while (++i < n->c)
		{
			if (node->puzzle[i] != closed->puzzle[i])
				break ;
		}
		if (i == n->c)
			return (1);
		closed = closed->next;
	}
	return (0);
}

void	free_state(npuzzle *n, state_list *node)
{
	free(node);
	//to continue
}

void	do_closed_list(npuzzle *n, t_a_star *a)
{
	state_list *node;
	state_list *old;
	state_list *tmp;

	node = a->open;
	old = NULL;
	while (node)
	{
		if (state_is_in_closed(n, a, node))
		{
			if (!old)
				a->open = node->next;
			else
				old->next = node->next;
			tmp = node->next;
			free_state(n, node);
			node = tmp;
		}
		else
		{
			old = node;
			node = node->next;
		}
	}
}

void	retrace_move_to_solve(state_list *node)
{
	if (!node->parent)
		return ;
	retrace_move_to_solve(node->parent);
	if (node->move == UP)
		ft_printf("UP\n");
	if (node->move == DOWN)
		ft_printf("DOWN\n");
	if (node->move == LEFT)
		ft_printf("LEFT\n");
	if (node->move == RIGHT)
		ft_printf("RIGHT\n");
}

void	end_function(npuzzle *n, state_list *node)
{
	ft_printf("g = %d\n", node->g);
	view_puzzle(n, node->puzzle);
	ft_printf("move to solve:\n");
	retrace_move_to_solve(node);
	quit("its a win\n");
}

void	a_star(npuzzle *n)
{
	t_a_star	a;
	state_list	*cur;
	int			i;

	a.open = creat_state_list(n, n->puzzle, NULL);
	a.closed = NULL;
	while (1)
	{
		cur = a.open;
		if (!cur)
			quit("open list is empty wtf\n");
		calc_fgh(n, cur);
		if (!cur->h)
			end_function(n, cur);
		creat_state_child(n, cur);
		i = -1;
		while (++i < cur->nb_child)
			a.open = add_state_to_list(a.open, cur->child[i]);
		a.open = cur->next;
		cur->next = a.closed;
		a.closed = cur;
		do_closed_list(n, &a);
		sort_by_f(&a);
	}
}
