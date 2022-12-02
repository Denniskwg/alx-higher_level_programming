#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - checks if a linked list has a cycle
 * @list: pointer to the start of a linked list
 * Return: 0 if no cycle 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	slow = list->next;
	fast = list->next;
	while (slow != NULL && fast != NULL && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}
