#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;
    
    int n;
    cin >> n;
    
    int total = 0;
    for (int i=1; i<=n; i++) {
        int num;
        cin >> num;

        if (num%2 != 0 && num%3 == 0) total += num;
    }
    cout << total;

    return 0;
}