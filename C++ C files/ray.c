#include <stdio.h>

int main(){
    int bun[5] = {5, 5, 6, 6, 6};

    for(int i = 0; i < 5; i++){
        printf("The Values: %d\n", bun[i]);
        printf("The address of this elements: %p\n", &bun[i]);
    }
}