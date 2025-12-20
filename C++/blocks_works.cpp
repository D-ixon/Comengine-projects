#include <iostream>
#include <string>

void myfuction(std::string fname) {
    std::cout << "Hello " << fname << std::endl;

}

int main() {
    myfuction("Liam");
    myfuction("Jenny");
    myfuction("Anja");
    return 0;
}