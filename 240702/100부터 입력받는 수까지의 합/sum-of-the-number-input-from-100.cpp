#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int n;
    cin >> n;

    int total = 0;
    for (int i=n; i<=100; i++) {
        total += i;
    }
    cout << total;
    
    return 0;
}