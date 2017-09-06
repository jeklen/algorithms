#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char *str;
    /* Initial memory allocation */
    str = (char *) malloc(15);
    strcpy(str, "tutorialspoint");
    printf("String = %s, Address = %u\n", str, str);
    strcpy(str, "tutorialspointokokokokok");
    printf("String = %s, Address = %u\n", str, str);

    free(str);

    return 0;
};
