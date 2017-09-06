/* A struct can be allocated automatically
 * but when using a pointer to struct which will not 
 * allocate space for the destination struct
 * when using it immediately, will get segfault
 */
#include <stdio.h>
#include <stdlib.h>

struct example {
    int foo;
};
int main()
{
    struct example e;
    e.foo = 1;
    printf("e.foo is %i\n", e.foo);

    struct example *f = malloc(sizeof(struct example));
    f->foo = 2;
    printf("f->foo is %i\n", f->foo);
    return 0;
}
