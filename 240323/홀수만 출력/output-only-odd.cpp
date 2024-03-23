#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int a, b;
    cin >> a >> b;

    for (int i=a; i>=a && i <=b; i+=2) {
        cout << i << ' ';
    }
    
    return 0;
}