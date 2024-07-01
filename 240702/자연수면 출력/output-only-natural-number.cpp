#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int a, b;
    cin >> a >> b;

    if (a>0) {
        for (int i=0; i<b; i++) cout << a;
    }
    else cout << 0;
    
    return 0;
}