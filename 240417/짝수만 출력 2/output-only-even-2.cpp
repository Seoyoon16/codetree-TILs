#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;
    
    int a, b;
    cin >> a >> b;

    int i = a;
    while (i >= b) {
        cout << i << ' ';
        i-=2;
    }
    return 0;
}