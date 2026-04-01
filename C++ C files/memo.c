#include <stdio.h>

int main() {
    int motors[4] = {10, 20, 30, 40};

    printf("Array Base Address: %p\n\n", (void*)motors);

    for (int i = 0; i < 4; i++) {
        printf("Index [%d]: Value = %d | Address = %p\n", i, motors[i], (void*)&motors[i]);
    }

    return 0;
}