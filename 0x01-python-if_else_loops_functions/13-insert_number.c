#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - a function in C that inserts a nun
 * @head: pointer to the head 
 * @number: number 
 * Return: the address of the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode1, *newnode2;

	newnode1 = (listint_t *)malloc(sizeof(listint_t));
	if (newnode1 == NULL)
		return (NULL);
	newnode2 = *head;
	newnode1->n = number;
	if (*head == NULL)
	{
		newnode1->next = *head;
		*head = newnode1;
		return (newnode1);
	}
	else if (newnode2->n > number)
	{
		newnode1->next = newnode2->next;
		*head = newnode1;
		return (newnode1);
	}
	while (newnode2->next)
	{
		if ((newnode2 + 1)->n > number)
		{
			newnode1->next = newnode2->next;
			newnode2->next = newnode1;
			return (newnode1);
		}
		else if ((newnode2 + 1)->next == NULL)
		{
			newnode1->next = (newnode2 + 1)->next;
			(newnode2 + 1)->next = newnode1;
			return (newnode1);
		}
	}
	return (NULL);
}
