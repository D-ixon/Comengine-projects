#include <iostream>

double calculateAverage(int numbers[], int size) {
    int sum = 0;

    for (int i = 0; i < size; i++) {
        sum += numbers[i]; 
    }

    return (double)sum / size;
}

int main() {

    int myGrades[5];
    for (int i = 0; i < 5; i++) {
        std::cin >> myGrades[i];
    }

    int numberOfGrades = 5;


    double average = calculateAverage(myGrades, numberOfGrades);


    std::cout << "The average grade is: " << average << std::endl;

    return 0;
} 