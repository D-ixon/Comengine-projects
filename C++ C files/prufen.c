#include <stdio.h>

int main() {
    int motor[5] = {10, 20, 30, 40, 50};
    int temp; 

    printf("--- Original Motor Speeds ---\n");
    for (int i = 0; i < 5; i++) {
        printf("Motor [%d]: %d RPM\n", i, motor[i]);
    }

    
    temp = motor[0];      
    motor[0] = motor[4];  
    motor[4] = temp;      

    printf("\n[SYSTEM]: Swap complete. First and Last elements exchanged.\n\n");

    printf("--- Updated Motor Speeds ---\n");
    for (int i = 0; i < 5; i++) {
        printf("Motor [%d]: %d RPM\n", i, motor[i]);
    }

    return 0;
}