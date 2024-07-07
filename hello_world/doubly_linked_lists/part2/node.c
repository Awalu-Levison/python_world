#include "head.h"

struct node *create_node()
{
	struct node *new_node = malloc(sizeof(struct node));
	new_node->prev = NULL;
	new_node->next = NULL;
	//new_node->data = data;
	return (new_node);
}
