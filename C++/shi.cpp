#include <iostream>
#include <string>

using namespace std;

void greetUser() {
    cout << "Hello! What is your name? ";
    string name;
    cin >> name;
    cout << "Nice to meet you, " << name << "!" << endl;
}

int main() {
    greetUser();
    return 0;
}