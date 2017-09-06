#include <stdio.h>
#include <stdlib.h>

int main()
{
    struct my_structure {
        char name[20];
        int number;
        int rank;
    };
    struct my_structure variable = {"Study Tonight", 35, 1};

    struct my_structure *ptr;
    ptr = &variable;

    printf("NAME: %s\n", ptr->name);
    printf("NUMBER: %d\n", ptr->number);
    printf("RANK: %d\n", ptr->rank);

    return 0;
}
