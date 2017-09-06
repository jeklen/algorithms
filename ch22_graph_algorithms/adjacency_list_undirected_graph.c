// A C program to demonstrate adjacency list representation of graphs

#include <stdio.h>
#include <stdlib.h>

// A structure to represent an adjacency list node
struct AdjListNode
{
    int dest;
    struct AdjListNode* next;
};
// A structure to represent an adjacency list
struct AdjList
{
    struct AdjListNode* head;   // pointer to head node of list
};

// A structure to represent a graph. A graph is an array of adjacent lsits
// Size of array will be V(number of vertices in V)
struct Graph
{
    int V;
    struct AdjList* array;
};
