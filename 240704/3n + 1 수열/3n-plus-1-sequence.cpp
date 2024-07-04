#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int N;
    cin >> N;

    int cnt = 0;
    while (true) {
        if (N == 1) break;

        if (N%2 == 0) N /= 2;
        else N = N * 3 + 1;
        cnt++;
    }
    cout << cnt;

    return 0;
}