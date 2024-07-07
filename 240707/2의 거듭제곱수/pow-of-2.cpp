#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int N;
    cin >> N;

    int x = 0;
    for (;;) {
        if (N == 1) break;
        N /= 2;
        x++;
    }
    cout << x;

    return 0;
}