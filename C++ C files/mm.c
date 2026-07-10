#include <stdio.h>

int main(){
    int a1_1, a1_2, a1_3, a2_1, a2_2, a2_3, a3_1, a3_2, a3_3, b1_1, b1_2, b2_1, b2_2, b3_1, b3_2;

    int c1_1, c1_2, c2_1, c2_2, c3_1, c3_2;

    printf("A matrix solver\n\n");
    printf("\n----------------Enter Enteries of A-----------------\n");

    printf("Row 1 column 1:  ");
    scanf("%d", &a1_1);

    printf("\nRow 1 column 2: ");
    scanf("%d", &a1_2);

    printf("\nRow 1 column 3: ");
    scanf("%d", &a1_3);

    printf("\nRow 2 column 1: ");
    scanf("%d", &a2_1);

    printf("\nRow 2 column 2: ");
    scanf("%d", &a2_2);

    printf("\nRow 2 column 3: ");
    scanf("%d", &a2_3);

    printf("\nRow 3 column 1: ");
    scanf("%d", &a3_1);

    printf("\nRow 3 column 2: ");
    scanf("%d", &a3_2);

    printf("\nRow 3 column 3: ");
    scanf("%d", &a3_3);

    printf("----------------Enter entries of B----------------\n\n");

    printf("\nRow 1 column 1: ");
    scanf("%d", &b1_1);
    
    printf("\nRow 1 column 2: ");
    scanf("%d", &b1_2);

    printf("\nRow 2 column 1: ");
    scanf("%d", &b2_1);

    printf("\nRow 2 column 2: ");
    scanf("%d", &b2_2);

    printf("\nRow 3 column 1: ");
    scanf("%d", &b3_1);

    printf("\nRow 3 column 2: ");
    scanf("%d", &b3_2);

    printf("\n-----------------Witness The Magic------------------\n\n");

    int a = (a1_1 * b1_1) + (a1_2 * b2_1) + (a1_3 * b3_1);
    int b = (a1_1 * b1_2) + (a1_2 * b2_2) + (a1_3 * b3_2);
    int c = (a2_1 * b1_1) + (a2_2 * b2_1) + (a2_3 * b3_1);
    int d = (a2_1 * b1_2) + (a2_2 * b2_2) + (a2_3 * b3_2);
    int e = (a3_1 * b1_1) + (a3_2 * b2_1) + (a3_3 * b3_1);
    int f = (a3_1 * b1_2) + (a3_2 * b2_2) + (a3_3 * b3_2);

    printf("C entry row 1 column 1 %d\n", a);
    printf("C entry row 1 column 2 %d\n", b);
    printf("C entry row 2 column 1 %d\n", c);
    printf("C entry row 2 column 2 %d\n", d);
    printf("C entry row 3 column 1 %d\n", e);
    printf("C entry row 3 column 2 %d\n", f);


}