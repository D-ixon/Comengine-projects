#include <iostream>
#include <string>

using namespace std;

void greetUser() {
    cout << "Hello! What is your name? ";
    string name;
    cin >> name;
    cout << "Nice to meet you, " << name << "!" << endl;
}

void myfunction(string name = "Hey"){
    cout<<"Hello YOu" << name << endl;
}

void multi(string fname, int smth){
    cout << "Hello " << fname << ", your number is " << smth << endl;

}

int sup(int a){
    return a*a;
}

int main() {
    greetUser();
    myfunction("Liam");
    myfunction("Jenny");
    myfunction();
    multi("Anja", 5);
    multi("Mark", 10);
    cout << sup(4);
    return 0;
}