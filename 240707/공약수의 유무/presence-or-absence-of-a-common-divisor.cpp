#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int a, b;
    cin >> a >> b;

    bool flag = false;
    for (int i=a; i<=b; i++) {
        if (1920%i == 0 && 2880%i == 0) flag = true;
    }

    if (flag) cout << 1;
    else cout << 0;
    
    return 0;
}