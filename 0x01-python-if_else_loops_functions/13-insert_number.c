#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"

/**
 * insert_node - to insert node
 * @head: head of the node
 * @number: number to be inserted
 * Return: NULL or new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *curr, *prev;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	curr = *head;
	prev = NULL;

	while (curr != NULL && curr->n < number)
	{
		prev = curr;
		curr = curr->next;
	}

	prev->next = new_node;
	new_node->next = curr;

	return (new_node);
}
