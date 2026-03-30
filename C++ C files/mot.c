#include <stdio.h>

int main() {
    int motor[4] = {500, 500};
    for(int i = 0; i < 4; i++){
        printf("Motor speeds: %d\n", motor[i]);
    }
    printf("Choose the speed you want motor 4th motor to reach based on: \n");
    printf("Take Off at 300RMP - 500RPM");
    printf("Hovering 500");
    printf("Some speed");
    
    scanf("%d", &motor[3]);

    for(int i = 0; i < 4; i++){
        printf("After User input, The new speeds of the User are: %d\n", motor[i]);

    }

    
}