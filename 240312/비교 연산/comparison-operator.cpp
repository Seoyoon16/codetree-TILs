#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int a, b;
    cin >> a >> b;

    if (a >= b) cout << 1 << endl;
    else cout << 0 << endl;

    if (a > b) cout << 1 << endl;
    else cout << 0 << endl;

    if (b >= a) cout << 1 << endl;
    else cout << 0 << endl;

    if (b > a) cout << 1 << endl;
    else cout << 0 << endl;

    if (a == b) cout << 1 << endl;
    else cout << 0 << endl;

    if (a != b) cout << 1;
    else cout << 0;

    return 0;
}

// // 의도
// cout << (a >= b) << endl;
// cout << (a > b) << endl;
// cout << (a <= b) << endl;
// cout << (a < b) << endl;
// cout << (a == b) << endl;
// cout << (a != b) << endl;