#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    int a = 3, b = 5, temp;
    temp = a;
    a = b;
    b = temp;
    std::cout << a << std::endl << b;
    return 0;
}