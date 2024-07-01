#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int a, b;
    cin >> a >> b;

    for (int i=a; i<=b; ) {
        cout << i << " ";
        if (i%2 != 0) i *= 2;
        else i += 3;
    }

    return 0;
}