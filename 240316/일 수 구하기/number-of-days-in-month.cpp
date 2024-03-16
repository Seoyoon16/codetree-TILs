#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;
    int n;
    cin >> n;

    if (n == 2) cout << 28;
    else if (n < 8 && n%2 == 0 || n >= 8 && n%2 == 1) cout << 30;
    else cout << 31;

    return 0;
}