#include <stdio.h>
#include <stdlib.h>

int main() {
    int num_elements, i;
    int *ptr;

    printf("Enter the number of elements: ");
    if (scanf("%d", &num_elements) != 1 || num_elements <= 0) {
        printf("Invalid input for number of elements.\n");
        return 1;
    }

    ptr = (int*) malloc(num_elements * sizeof(int));

    if (ptr == NULL) {
        printf("Error! Memory not allocated.\n");
        return 1; 
    }

    printf("Enter %d elements:\n", num_elements);
    for (i = 0; i < num_elements; ++i) {
        printf("Element %d: ", i + 1);
        scanf("%d", (ptr + i)); 
    }

    printf("\nDisplaying elements:\n");
    for (i = 0; i < num_elements; ++i) {
        printf("Element %d value: %d, stored at address: %p\n", i + 1, *(ptr + i), (void*)(ptr + i));
    }
    free(ptr);
    ptr = NULL; 

    printf("\nMemory freed. Program finished.\n");

    return 0;
}
