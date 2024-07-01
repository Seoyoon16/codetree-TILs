#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int n; int i=0; int cnt=0;
    while (i<10) {
        cin >> n;
        if (n%2 == 1) cnt += 1;
        i++;
    }
    cout << cnt;

    return 0;
}