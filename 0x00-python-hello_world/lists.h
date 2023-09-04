#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - for singly linked list
 * @n: for integer
 * @next: A pointer for the next node
 *
 * Description: thos the singly linked list node 
 * structure for the Holberton project
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* lists.h files*/