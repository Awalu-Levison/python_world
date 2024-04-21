#include "main.h"
/**
 * main - Access the node
 * Return: 0 on success
 */
int main(void)
{
	struct node *head = NULL;
	struct node *ptr;
	head = add_empty(head, 45);
	head = add_first(head, 44);

	ptr = head;
	while (ptr != NULL)
	{
		printf("%d ", head->data);
		ptr = ptr->next;
	}
	return (0);

}
