#include <stdio.h>

#define MAX 5

int deque[MAX];
int front = -1, rear = -1;

void frontInsert(int item)
{
    if(front == 0)
    {
        printf("Overflow\n");
        return;
    }

    if(front == -1)
        front = rear = 0;
    else
        front--;

    deque[front] = item;
}

void rearInsert(int item)
{
    if(rear == MAX - 1)
    {
        printf("Overflow\n");
        return;
    }

    if(front == -1)
        front = rear = 0;
    else
        rear++;

    deque[rear] = item;
}

void frontDelete()
{
    if(front == -1)
    {
        printf("Underflow\n");
        return;
    }

    printf("Deleted: %d\n", deque[front]);

    if(front == rear)
        front = rear = -1;
    else
        front++;
}

void rearDelete()
{
    if(front == -1)
    {
        printf("Underflow\n");
        return;
    }

    printf("Deleted: %d\n", deque[rear]);

    if(front == rear)
        front = rear = -1;
    else
        rear--;
}
