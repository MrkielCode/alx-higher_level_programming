#include "lists.h"
/**
 * check_cycle - To check node
 * @list: nodes
 * Return: 1 or 0
 */

int check_cycle(listint_t *list)
{
	listint_t *slow_node = list;
	listint_t *fast_node = list;

	if (!list)
		return (0);

	while (slow_node && fast_node && fast_node->next)
	{
		slow_node = slow_node->next;
		fast_node = fast_node->next->next;
		if (slow_node == fast_node)
		{
			return (1);
		}
	}
	return (0);
}
