#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int a, b, temp;
    cin >> a >> b;
    temp = a;
    a = b;
    b = temp;
    cout << a << ' ' << b;
    return 0;
}