#include "lists.h"

/**
 * insert_node - A function that insert a number
 * in a sortyed linked list
 * @head: Pointer to the first node of the list
 * @number: Data to be inserted into the list
 * Return: Address of New node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new_node = NULL;
	listint_t *temp_ptr = NULL;

	if (!head)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (!new_node) /*Check mem-allocation*/
		return (NULL);

	new_node->n = number; /*Initialise n with number*/
	new_node->next = NULL;

	if (!*head || (*head)->n > number)
	{
		new_node->next = *head;
		return (*head = new_node);
	}
	else
	{
		/*Iterate through each number in the list*/
		while (current && current->n < number)
		{
			temp_ptr = current;
			current = current->next;
		}
		temp_ptr->next = new_node;
		new_node->next = current;
	}
	return (new_node);
}
