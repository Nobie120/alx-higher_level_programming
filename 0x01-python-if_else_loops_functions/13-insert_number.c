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

	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	node->n = number;
	node->next = NULL;
	if (!current || current->n >= number)
	{
		node->next = current;
		*head = node;
		return(node);
	}
	while (current && current->n < number)
	{
		previous = current;
		current = previous->next;
	}
	if (!current || current->n > number)
	{
		previous->next = node;
		node->next = current;
		return (node);
	}
	free_listint(node);
	return (NULL);
}
