#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * is_palindrome - checks if a singly linked list
 * is a palindrome
 * @head: pointer to first node of a singly linked list
 * Return: 0 if not palindrome 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *prev, *current, *ptr = NULL;
	int i = 0;
	int n[100];

	if (*head == NULL)
		return (1);
	current = *head;
	while (current != NULL)
	{
		n[i] = current->n;
		current = current->next;
		i++;
	}
	current = *head;
	while (current != NULL)
	{
		prev = current;
		if (current == *head)
			current = current->next;
		else
			current = ptr;
		ptr = current->next;
		current->next = prev;
		if (prev == *head)
			prev->next = NULL;
		if (ptr == NULL)
			break;
	}
	*head = current;
	i = 0;
	ptr = *head;
	while (ptr != NULL)
	{
		if (ptr->n != n[i])
			return (0);
		i++;
		ptr = ptr->next;
	}
	return (1);
}
