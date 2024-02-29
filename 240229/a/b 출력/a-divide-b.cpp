#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int a, b;
    cin >> a >> b;

    

    int res = 0;
    cout << a / b << '.';
    for (int i=0; i <20; i++) {
        a = (a % b) * 10;
        res = a / b;
        cout << res;

    }
    return 0;
}