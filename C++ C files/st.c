#include <stdio.h>

int main() {
    int x = 14;
    int *p= &x;

    printf("The address of x is: %p\n", (void*)&x);

    return 0;
}