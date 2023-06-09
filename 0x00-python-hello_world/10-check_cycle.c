#include "lists.h"

/**
 * check_cycle - checks if the singly linked list has a cycle in it
 * @list: a pointer to the head of list.
 * Return: 0 if there is no cycle, 1 if a cycle exit
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list || !list->next)
		return (0);

	slow = list;
	fast = list->next;

	while (slow && fast && fast->next)
	{
		if (slow == fast)
			return (1);

		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}
