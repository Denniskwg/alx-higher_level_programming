#include "lists.h"
/**
 * check_cycle - checks if a linked list has a cycle
 * @list: pointer to the start of a linked list
 * Return: 0 if no cycle 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current;
	listint_t *temp;

	current = list;
	while (current != NULL)
	{
		if (current == list)
			temp = list->next;
		else
			temp = list;
		while (temp != list && temp != NULL)
		{
			if (temp->next == current)
				return (1);
			temp = temp->next;
		}
		if (temp == list)
			return (1);
		if (temp == NULL)
			return (0);
		current = current->next;
	}
	temp = current->next;
	while (current != NULL && current != list)
	{
		while (temp != NULL && temp != list)
		{
			if (current->next == temp)
				return (1);
			temp = temp->next;
		}
		current = current->next;
	}
	return (0);
}
