#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int n;
    cin >> n;

    bool flag = true;
    for (int i=2; i<n; i++) {
        if (n%i == 0) flag = false;
    }

    if (flag) cout << 'P';
    else cout << 'C';
    
    return 0;
}