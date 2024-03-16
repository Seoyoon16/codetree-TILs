#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int cnt = 0;
    for (int i=0; i<3; i++) {
        char sym; int tem;
        cin >> sym >> tem;

        if (sym == 'Y' && tem >= 37) {
            cnt++;
        }
    }
    if (cnt >= 2) cout << 'E';
    else cout << 'N';

    return 0;
}