#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int n;
    cin >> n;

    for (int i=n; i<=5*n; i+=n) {
        cout << i << ' ';
    }
    return 0;
}