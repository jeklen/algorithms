#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

void swap(int *xp, int *yp)
{
    int tmp = *xp;
    *xp = *yp;
    *yp = tmp;
}

void bubbleSort(int arr[], int length)
{
    int i;
    bool swapped = true;
    while (swapped) {
        swapped = false;
        for (i=0; i<length-1; ++i) {
            if (arr[i] > arr[i+1]) {
                swap(&arr[i], &arr[i+1]);
                swapped = true;
            }
        }
    }
}

void printArray(int arr[], int length)
{
    int i;
    for (i=0; i<length; i++) {
        printf("%i ", arr[i]);
    }
    printf("\n");
}

int main()
{
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int length = sizeof(arr)/sizeof(arr[0]);
    printArray(arr, length);
    bubbleSort(arr, length);
    printArray(arr, length);
    return 0;
}
