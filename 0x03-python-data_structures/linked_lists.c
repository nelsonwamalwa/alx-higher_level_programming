#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - This prints all the elements
 *  of a listint_t list
 * @h: The pointer to head of a list
 * Return: The number of nodes
 */
size_t print_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int n; /* The number of nodes */

    current = h;
    n = 0;
    while (current != NULL)
    {
	printf("%i\n", current->n);
	current = current->next;
	n++;
    }

    return (n);
}

/**
 * add_nodeint_end - This adds a new node at 
 * the end of a listint_t list
 * @head: pointer to pointer of the
 * first node of listint_t list.
 * @n: the integer to be included in the new node
 * Return: the address of the new element or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
    listint_t *new;
    listint_t *current;

    current = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
	return (NULL);

    new->n = n;
    new->next = NULL;

    if (*head == NULL)
	*head = new;
    else
    {
	while (current->next != NULL)
	    current = current->next;
	current->next = new;
    }

    return (new);
}

/**
 * free_listint - Thsi frees a listint_t list
 * @head: points to a list to be freed
 * Return: Is void
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
	current = head;
	head = head->next;
	free(current);
    }
}