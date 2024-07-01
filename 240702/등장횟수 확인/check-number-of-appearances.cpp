#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int i = 0; int cnt = 0;
    while (i<5) {
        int num;
        cin >> num;

        if (num%2 == 0) cnt++;
        i ++;
    }
    cout << cnt;
    return 0;
}