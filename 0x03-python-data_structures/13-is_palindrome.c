#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is
 * a palindrome
 * @head: pointer to start of a linked list
 * Return: 0 if not palindrome 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current, *temp, *new;
	int i = 0, j, length;
	
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	current = *head;
	while (current != NULL)
	{
		i++;
		current = current->next;
	}
	length = i;
	i = i / 2;
	current = *head;
	while (i > 1)
	{
		current = current->next;
		i--;
	}
	temp = current->next;
	current->next = NULL;
	if (length % 2 == 0)
		new = temp;
	else
		new = temp->next;
	reverse(head);
	current = *head;
	while (current != NULL && new != NULL)
	{
		if (current->n != new->n)
		{
			j = 0;
			break;
		}
		current = current->next;
		new = new->next;
		j = 1;
	}
	reverse(head);
	current = *head;
	while (current->next != NULL)
		current = current->next;
	current->next = temp;
	return (j);
}

/**
 * reverse - reverses a linked list
 * @head - pointer to the start of a linked list
 */
void reverse(listint_t **head)
{
	listint_t *current, *next, *prev;

	prev = NULL;
	current = *head;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}
