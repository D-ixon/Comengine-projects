#include <stdio.h>

void swap(int *a, int *b) {
    int initial = *a;
    *a = *b;
    *b = initial;
}

int main() {
    int a, b;

    printf("Hello, Please Enter two numbers a and b Below:\n");
    scanf("%d %d", &a, &b);

    printf("Before swap: %d %d\n", a, b);

    swap(&a, &b);
    printf("After the swap: %d %d\n", a, b);

    return 0;
}