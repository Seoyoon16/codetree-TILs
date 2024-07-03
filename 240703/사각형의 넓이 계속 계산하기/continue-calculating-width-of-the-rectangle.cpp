#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int w, h; char c;

    while (true) {
        cin >> w >> h >> c;
        int area = w * h;
        cout << area << endl;
        if (c == 'C') break;
    }

    return 0;
}