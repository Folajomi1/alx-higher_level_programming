#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: The head of the singly linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *start = *head;
    listint_t *end = start;
    int len = 0;

    if (head == NULL || *head == NULL)
        return (1);  // An empty list is considered a palindrome

    // Find the length of the linked list
    while (end != NULL)
    {
        len++;
        end = end->next;
    }

    end = *head;

    // Compare elements from the start and end of the list towards the center
    for (int i = 0; i < len / 2; i++)
    {
        if (start->n != get_nodeint_at_index(end, len - i - 1)->n)
            return (0);
        
        start = start->next;
    }

    return (1);
}

/**
 * get_nodeint_at_index - Gets a node from a linked list
 * @head: The head of the linked list
 * @index: The index to find in the linked list
 *
 * Return: The specific node of the linked list
 */
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
    listint_t *current = head;
    unsigned int iter_times = 0;

    while (current != NULL)
    {
        if (iter_times == index)
            return (current);

        current = current->next;
        ++iter_times;
    }

    return (NULL);
}

/**
 * listint_len - Counts the number of elements in a linked list
 * @h: The linked list to count
 *
 * Return: Number of elements in the linked list
 */
size_t listint_len(const listint_t *h)
{
    size_t length = 0;

    while (h != NULL)
    {
        ++length;
        h = h->next;
    }

    return (length);
}
