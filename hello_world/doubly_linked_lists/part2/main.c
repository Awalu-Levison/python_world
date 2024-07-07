#include "head.h"
/**
 * main - Accessing the node
 * Return: 0 on success
 */
int main(void)
{
	struct node *head = NULL;
	head = create_node(head, 70);

	printf("List is: %d\n", (*head).data);
	return (0);
}
