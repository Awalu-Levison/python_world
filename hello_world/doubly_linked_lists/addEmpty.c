#include "main.h"
/**
 * add_toEmptylist- Adding a node the empty list
 * in Doubly linked list in C
 * @head: Reference to the newly added element
 * @data: The data (element) given to the list
 * Return: New list
 */
struct node *add_empty(struct node *head, int data)
{
	/*Define a temporary var for traversing the node pointers*/
	struct node *temp = malloc(sizeof(struct node));
	temp->prev = NULL;
	temp->next = NULL;
	temp->data = data;
	head = temp;
	return (head);
}
