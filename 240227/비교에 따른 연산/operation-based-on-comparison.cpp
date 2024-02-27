#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;
    int a, b;
    cin >> a >> b;
    
    if (a > b) {
        cout << a * b;
    }
    else {
        cout << b / a;
    }
    return 0;
}