#include <stdio.h>

int F(int x)
{
    if (x == 0)
        return 0;
    else
        return 2 * F(x - 1) + x * x;
}

int main() {
    printf("%i", F(-1));
    return 0;
}
