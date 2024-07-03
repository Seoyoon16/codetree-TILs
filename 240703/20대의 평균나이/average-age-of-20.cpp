#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int age;
    int total = 0; int cnt = 0;

    while (true) {
        cin >> age;
        if (age >= 30) break;
        total += age;
        cnt++;
    }

    cout << fixed;
    cout.precision(2);
    cout << total/float(cnt);

    return 0;
}