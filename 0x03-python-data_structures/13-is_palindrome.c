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
	listint_t *current;
	int i = 0, j = 0;
	int *n;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	current = *head;
	
	while (current != NULL)
	{
		j++;
		current = current->next;
	}
	n = malloc(sizeof(int) * j);
	if (n == NULL)
		return (0);
	while (current != NULL)
	{
		n[i] = current->n;
		current = current->next;
		i++;
	}
	current = *head;
	i--;
	while (current != NULL)
	{
		if (current->n != n[i])
			return (0);
		i--;
		current = current->next;
	}
	free(n);
	return (1);
}
