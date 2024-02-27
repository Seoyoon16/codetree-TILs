#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;
    int n;
    cin >> n;
    
    if (n >= 80) cout << "pass";
    else cout << 80-n << " more score";
    return 0;
}