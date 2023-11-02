#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>
#include <string.h>
#include <stdio.h>
/**
 * struct listint_s - singly linked list
 * @i: integer
 * @next: points to the next node
 */
typedef struct listint_s
{
	int i;
	struct listint_s *next;
} listint_t;

int main(void);
size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int i);
void free_listint(listint_t *head);
listint_t *insert_node(listint_t **head, int number);

#endif
