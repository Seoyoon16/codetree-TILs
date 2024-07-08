#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int n;
    int i = 0;
    bool flag = true;

    while (i < 5) {
        cin >> n;
        if (n%3 != 0) flag = false;
        i++;
    }

    if (flag) cout << 1;
    else cout << 0;
    
    return 0;
}