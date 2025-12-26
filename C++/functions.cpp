#include <iostream>
using namespace std;


int doubleGame(int x) {
  return x * 2;
}

void changeValue(int &num) {
  num = 50;
}

void swapNums(int &x, int &y) {
  int z = x;
  x = y;
  y = z;
}

void samechange(string &word){
    word += "Kofi";
}


int main() {
  for (int i = 1; i <= 5; i++) {
    cout << "Double of " << i << " is " << doubleGame(i) << endl;
  }

  int value = 10;
  changeValue(value);  // Call the function and change the value to 50
  cout << value <<endl;

  int firstNum = 10;
  int secondNum = 20;

  cout << "Before swap: " << "\n";
  cout << firstNum <<"  "<< secondNum << "\n";

  // Call the function, which will change the values of firstNum and secondNum
  swapNums(firstNum, secondNum);

  cout << "After swap: " << "\n";
  cout << firstNum <<" "<<secondNum << "\n";

  string myword = "Dickson";
    samechange(myword);
    cout << myword <<endl;



  return 0;
}

