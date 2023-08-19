#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *reverse_my_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_my_list - To reverses a linked list
 * @head: head pointer
 * Return: prev
 */

listint_t *reverse_my_list(listint_t *head)
{
	listint_t *pv = NULL, *cr = head, *next = NULL;

	while (cr != NULL)
	{
		next = cr->next;
		cr->next = pv;
		pv = cr;
		cr = next;
	}
	return (pv);
}

/**
 * is_palindrome - Checks list is palindrone
 * @head: head
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *sl = *head;
	listint_t *ft = *head;
	listint_t *half2 = reverse_my_list(sl->next);
	listint_t *half1 = *head;
	 listint_t *half2_copy = half2;

	if (*head == NULL || (*head)->next == NULL)
		return (1);


	while (ft->next != NULL && ft->next->next != NULL)
	{
		sl = sl->next;
		ft = ft->next->next;
	}

	int is_palindrome = 1;

	while (half2_copy != NULL)
	{
		if (half1->n != half2_copy->n)
		{
			is_palindrome = 0;
			break;
		}
		half1 = half1->next;
		half2_copy = half2_copy->next;
	}
	sl->next = reverse_my_list(half2);
	return (is_palindrome);
}
