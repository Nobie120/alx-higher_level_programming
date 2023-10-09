#include "lists.h"
/**
 * linked_list - checks if a singly linked list is a palindrome.
 * @head:pointer to the linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL || head == NULL)
		return (1);
	return (palindrome(head, *head));
}

/**
 * palindrome - compare data in linkedlist
 * to find out if its a palindrome
 * @head:poitner to the linked list
 * @currrent:pointer to a node in the linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int palindrome(listint_t **head, listint_t *current)
{
	if (current == NULL)
		return (1);
	if (palindrome(head, current->next) && ((*head)->n == current->n))
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
