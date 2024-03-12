#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int a, b, c;
    cin >> a >> b >> c;

    if (a <= b && a <= c) cout << a;
    else if (b <= a && b <= c) cout << b;
    else if (c <= a && c <= b) cout << c;

    return 0;
}