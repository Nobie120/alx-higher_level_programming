#include "lists.h"

/**
 * insert_node -  function in C that inserts a number
 * into a sorted singly linked list.
 * @number:the number to be added
 * @head:pointer to the linked list
 *
 * Return:NULL if failed pointer to
 * the added node if succesfull
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *previous = *head;
	listint_t *node;

	if (!head)
		return(NULL);
	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);

	while (current && previous)
	{
		previous = current;
		current = previous->next;
		if (current->n >= number && previous->n <= number)
		{
			node->next = current;
			previous->next = node;
			node->n = number;
			return (previous->next);
		}
	}
	return (NULL);
}
