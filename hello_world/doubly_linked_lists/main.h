#ifndef MAIN_H
#define MAIN_H

#include <stdio.h>
#include <stdlib.h>

/**
 * struct node - A structure for doubly linked list
 * @prev: Pointer to the previous element
 * @data: The type of data defined in the structure
 * @next: Pointer to the next element
 *
 * Description: A doubly linked list pratice in C
 */
struct node
{
	struct node *prev; /**pointer for previous element*/
	int data; /*Data defined could be anything*/
	struct node *next; /* Pointer to the next element of a list*/
};

struct node *add_empty(struct node *head, int data);
struct node *add_first(struct node *head, int data);

#endif /*By: Awalu Levison*/
