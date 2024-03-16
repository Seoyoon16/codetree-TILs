#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int m1, e1, m2, e2;
    cin >> m1 >> e1 >> m2 >> e2;

    if (m1 > m2) cout << 'A';
    else if (m1 == m2) {
        if (e1 > e2) cout << 'A';
        else cout << 'B';
    }
    else cout << 'B';
    return 0;
}