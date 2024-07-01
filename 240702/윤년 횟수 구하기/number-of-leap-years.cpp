#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int n; int day = 0;
    cin >> n;

    for (int i=1; i<=n; i++) {
        if (i%4 != 0 || i%100 == 0 && i%400 != 0) day += 1;
    }
    cout << n-day;

    return 0;
}