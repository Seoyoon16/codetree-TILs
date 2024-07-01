#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int a, b;
    cin >> a >> b;

    int total = 0;
    for (int i=a; i<=b; i++) {
        total += i;
    }
    cout << total;
    
    return 0;
}