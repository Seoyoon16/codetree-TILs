#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int n;
    cin >> n;

    int cnt = 0; int m = n;
    for (int i=1; i<=m; i++) {
        n /= i;
        cnt++;
        // cout << n << ", " << i << ", " << cnt << endl; 
        if (n <= 1) {
            cout << cnt;
            break;
        }
    }

    return 0;
}