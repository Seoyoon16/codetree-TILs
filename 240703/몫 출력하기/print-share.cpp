#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int n = 0;
    int cnt = 0;

    while (true) {
        cin >> n;
        if (n%2 == 1) continue;
        else {
            cout << n/2 << endl;
            cnt++;
            if (cnt >= 3) break;
        }
    }
    return 0;
}