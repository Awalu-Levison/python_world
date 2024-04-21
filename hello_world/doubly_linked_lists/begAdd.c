#include "main.h"
/**
 * add_first_node - A function that add node
 * to the beginning of the doubly linked list
 * @head: Reference to the head node of a list
 * @data: The data defined in the list
 * Return: Newly added node
 */
struct node *add_first(struct node *head, int data)
{
	struct node *temp = malloc(sizeof(struct node));
	temp->prev = NULL;
	temp->data = data;
	temp->next = NULL;
	temp->next = head;
	head->prev = temp;
	head = temp;
	return (head);
}
