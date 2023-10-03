#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list:the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *previous = list, *current = list;

	if (!list)
	{
		free_listint(list);
		return (0);
	}
	while (current && current->next)
	{
		previous = previous->next;
		current = current->next->next;
		if (current == previous)
			return (1);
	}
	return (0);
}
