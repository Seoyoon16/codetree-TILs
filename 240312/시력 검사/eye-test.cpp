#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;
    
    float r, l;
    cin >> r >> l;

    if (r >= 1.0 && l >= 1.0) cout << "High";
    else if (r >= 0.5 && l >= 0.5) cout << "Middle";
    else cout << "Low";
    
    return 0;
}