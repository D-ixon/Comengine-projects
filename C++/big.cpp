#include <iostream>

// This function takes an array and its size as "ingredients"
// it returns a double (a number with decimals)
double calculateAverage(int numbers[], int size) {
    int sum = 0;

    for (int i = 0; i < size; i++) {
        sum += numbers[i]; // Adding each element to the sum
    }

    // We divide the sum by the number of elements to get the average
    // We use (double) to make sure the division is precise
    return (double)sum / size;
}

int main() {
    // 1. We define an array of integers
    int myGrades[] = {85, 90, 78, 92, 88};
    
    // 2. We calculate how many items are in the array
    int numberOfGrades = 5;

    // 3. We call our function and store the 'returned' value in a variable
    double average = calculateAverage(myGrades, numberOfGrades);

    // 4. Print the result
    std::cout << "The average grade is: " << average << std::endl;

    return 0;
}