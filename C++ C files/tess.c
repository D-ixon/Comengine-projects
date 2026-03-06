#include <stdio.h>

int main() {
    int x = 14;
    int *p= &x;
    int y = 56;
    int *u = &y;
    int z = 78;
    int *v = &z;

    printf("The address of x is: %p\n", (void*)&x);
    printf("Adress %p\n", (void*)&y);
    printf("Adress %p\n", (void*)&z);

    return 0;
}