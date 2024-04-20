#include "lists.h"

void iterate_revers(listint_t **head);
int list_comp(listint_t *head, listint_t *middle_list, int length);
int is_palindrome(listint_t **head);
/**
 * is_palindrome - Checks if the linked list is palindrome
 * @head: Pointer to the first node of the linked list
 * Return: 0 on failure or 1 on success
 */
int is_palindrome(listint_t **head)
{
	int i, j; /*i: length*/
	listint_t *middle;
	listint_t *temp;

	if (head == NULL || *head == NULL)
		return (1);

	middle = *head;
	temp = *head;

	for (i = 0; temp != NULL; i++)
		temp = temp->next;

	i = i / 2;
	for (j = 1; j < i; j++)
		middle = middle->next;

	if (i % 2 != 0 && j != 1)
	{
		middle = middle->next;
		i -= 1;
	}
	iterate_revers(&middle);
	j = list_comp(*head, middle, i);
	return (j);
}

/**
 * list_comp - Compare linked list
 * @head: Pointer to the first node
 * @middle_list: The middle list
 * @length: The length of the list
 * Return: 1 if it is palindrome or 0 if not.
 */
int list_comp(listint_t *head, listint_t *middle_list, int length)
{
	int i;

	if (head == NULL || middle_list == NULL)
		return (1);

	for (i = 0; i < length; i++)
	{
		if (head->n != middle_list->n)
			return (0);
		head = head->next; /*iterate head pointer*/
		middle_list = middle_list->next;
	}
	return (1);
}

/**
 * iterate_revers - Iterate the linked list reverse mode
 * @head: Pointer to the first node
 */
void iterate_revers(listint_t **head)
{
	listint_t *current_ptr;
	listint_t *next_ptr;
	listint_t *prev_ptr;

	if (head == NULL || *head == NULL)
		return;

	prev_ptr = NULL;
	current_ptr = *head;

	while (current_ptr != NULL)
	{
		next_ptr = current_ptr->next;
		current_ptr->next = prev_ptr;
		prev_ptr = current_ptr;
		current_ptr = next_ptr;
	}
	*head = prev_ptr;
}
