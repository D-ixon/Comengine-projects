#include <iostream>

using namespace std;

int doubleGame(int x) {
  return x * 2;
}
void changeValue(int &num) {
  num = 50;
}

int main() {
  for (int i = 1; i <= 5; i++) {
    cout << "Double of " << i << " is " << doubleGame(i) << endl;
  }

  int value = 10;
  changeValue(value);  // Call the function and change the value to 50
  cout << value <<endl;

  return 0;
}