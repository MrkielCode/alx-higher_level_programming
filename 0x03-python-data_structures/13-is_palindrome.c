#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
	return (*head);
}

int is_palindrome(listint_t **head)
{
	listint_t *sl = *head, *ft = *head;
	listint_t *prev_sl = NULL, *mid = NULL;
	listint_t *second_half, *temp;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (ft != NULL && ft->next != NULL)
	{
		ft = ft->next->next;
		prev_sl = sl;
		sl = sl->next;
	}
	if (ft != NULL)
	{
		mid = sl;
		sl = sl->next;
	}
	second_half = sl;
	prev_sl->next = NULL;
	reverse_listint(&second_half);
	temp = *head;
	while (second_half != NULL)
	{
		if (temp->n != second_half->n)
		{
			is_palindrome = 0;
			break;
		}
		temp = temp->next;
		second_half = second_half->next;
	}
	reverse_listint(&sl);
	if (mid != NULL)
	{
		prev_sl->next = mid;
		mid->next = sl;
	} else
		prev_sl->next = sl;
	return (is_palindrome);
}
