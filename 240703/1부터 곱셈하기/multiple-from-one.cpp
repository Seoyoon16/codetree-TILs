#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int n;
    cin >> n;

    int prod = 1;
    int i = 1;

    while (i<=10) {
        prod *= i;
        if (prod >= n) break;
        i++;
    }
    cout << i;

    return 0;
}