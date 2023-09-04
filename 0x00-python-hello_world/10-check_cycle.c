#include "lists.h"

/**
 * check_cycle - This checks if agiven
 * linked list contains a cycle
 * @list: this a linked list to check
 *
 * Return: 1 if the given list has a cycle,
 * 0 if the list doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}