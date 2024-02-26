#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int a, b;
    double c;
    cin >> a >> b;
    
    c = double(a + b) / (a - b);
    
    cout << fixed;
    cout.precision(2);
    cout << c;
    return 0;
}