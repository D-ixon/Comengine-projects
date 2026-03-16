#include <stdio.h>

int main() {
    int a = 10;
    int *ptr = &a;

    printf("The address of a is: %p\n", (void*)ptr);
}