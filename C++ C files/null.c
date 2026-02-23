#include <stdio.h>

int main() {

    int myArray[10] = {10, 20, 30, 40, 50}; 

    myArray[5] = 60;
    
    int size = sizeof(myArray) / sizeof(myArray[0]);

    printf("Elements in the array are: \n");
    for (int i = 0; i < size; i++) {
        printf("%d\n", myArray[i]); 
    }
    
    printf("\n"); 
    
    return 0;
}
