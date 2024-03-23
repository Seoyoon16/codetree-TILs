#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int a, b;
    cin >> b >> a;

    for (int i=b; i>=a; i-=2) cout << i << ' ';

    return 0;
}