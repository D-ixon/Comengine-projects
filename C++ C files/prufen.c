#include <stdio.h>


int main() {
    int motor[3] = {100, 80};

    printf("\nSwapping Values in an array\n");

    for (int i = 0; i < 1; i++){
        int value = motor[i];
        printf("%d\n", value);
    }
    for (int i = 1; i < 2; i++){
        int dos = motor[i];
        printf("%d\n\n", dos);
    }

    return 0;
}