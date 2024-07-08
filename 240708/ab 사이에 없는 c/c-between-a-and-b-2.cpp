#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int a, b, c;
    cin >> a >> b >> c;

    bool flag = true;
    for (int i=a; i<=b; i++) {
        if (i%c == 0) flag = false;
    }

    if (flag) cout << "YES";
    else cout << "NO";
    return 0;
}