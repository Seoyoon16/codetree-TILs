#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    int a = 5, b = 6, c = 7;
    int temp1, temp2;
    temp1 = b; temp2 = c;
    b = a;
    c = temp1;
    a = temp2;

    std::cout << a << std::endl << b << std::endl << c;

    // // 교체
	// int temp = a;
	// a = c;
    // c = b;
	// b = temp;
    
    return 0;
}