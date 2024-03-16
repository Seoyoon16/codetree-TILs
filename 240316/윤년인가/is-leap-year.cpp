#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;
    int y;
    cin >> y;

    if (y%4 == 0) {
        if (y%100 == 0 && y%400 != 0) cout << "false";
        else cout << "true";
    }
    else cout << "false";

    return 0;
}