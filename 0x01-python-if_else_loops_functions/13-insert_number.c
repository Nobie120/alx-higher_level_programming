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
	listint_t *current = *head;
	listint_t *node;

	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	node->n = number;
	node->next = NULL;

	if (!current || node->n < current->n)
	{
		node->next = node;
		return (*head = node);
	}

	while(current)
	{
		if(!current->next || node->n < current->next->n)
		{
			node->next = current->next;
			current->next = node;
			return(node);
		}
		current = current->next;
	}
	return (NULL);
}
