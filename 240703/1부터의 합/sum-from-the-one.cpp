#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int n;
    cin >> n;

    int total = 0;
    int i = 1;

    while (i<=100) {
        total += i;
        if (total >= n) break;
        i++;
    }
    cout << i;

    return 0;
}