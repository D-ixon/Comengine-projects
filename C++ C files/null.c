#include <stdio.h>

int main() {

    int myArray[] = {10, 20, 30, 40, 50}; 
    
    int size = sizeof(myArray) / sizeof(myArray[0]);

    printf("Elements in the array are: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", myArray[i]); 
    }
    
    printf("\n"); 
    
    return 0;
}
