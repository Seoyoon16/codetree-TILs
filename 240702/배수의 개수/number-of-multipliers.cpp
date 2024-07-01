#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int cnt1 = 0; int cnt2 = 0;
    for (int i=0; i<10; i++) {
        int n;
        cin >> n;

        if (n%3 == 0) cnt1 += 1;
        if (n%5 == 0) cnt2 += 1;
    }
    cout << cnt1 << " " << cnt2;

    return 0;
}