#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int n;
    cin >> n;

    int i = 3;
    while (i <= n) {
        cout << i << ' ';
        i+=3;
    }
    return 0;
}