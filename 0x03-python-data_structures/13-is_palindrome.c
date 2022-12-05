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
	int i = 0, j = 0;
	int n[20];

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	current = *head;
	while (current != NULL)
	{
		prev = current;
		n[i] = current->n;
		i++;
		if (current == *head)
			current = current->next;
		else
			current = ptr;
		ptr = current->next;
		current->next = prev;
		if (prev == *head)
			prev->next = NULL;
		if (ptr == NULL)
		{
			n[i] = current->n;
			break;
		}
	}
	*head = current;
	while (current != NULL)
	{
		if (current->n != n[j])
			return (0);
		j++;
		current = current->next;
	}
	return (1);
}
