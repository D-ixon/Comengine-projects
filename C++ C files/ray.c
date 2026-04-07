#include <stdio.h>

int main(){
    int bun[5] = {5, 5, 6, 6, 6};

    for(int i = 0; i < 5; i++){
        // We add a second %d to catch the second variable (bun[i])
        printf("Index [%d] | Value: %d\n", i, bun[i]);
        
        // We add a %d for the index and a %p for the address
        printf("Index [%d] | Address: %p\n", i, (void*)&bun[i]);
        
        printf("--------------------------\n");
    }
    
    return 0;
}