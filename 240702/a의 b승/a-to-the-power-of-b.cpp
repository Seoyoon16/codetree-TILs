#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int a, b;
    cin >> a >> b;

    int prod = 1;
    for (int i=1; i<=b; i++) prod *= a;

    if (b == 0) cout << 1;
    else cout << prod;

    return 0;
}