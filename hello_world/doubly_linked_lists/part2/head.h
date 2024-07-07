#ifndef HEAD_H
#define HEAD_H

#include <stdio.h>
#include <stdlib.h>

/**
 * node - Thr structure of doubly linked list
 * @prev: Reference to predvious element
 * @next: Reference to the next element
 * @data: The data defined
 */
struct node
{
	struct node *prev;
	struct node *next;
	int data;
};
struct node *create_node();


#endif
