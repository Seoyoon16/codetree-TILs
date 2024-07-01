#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int a, b;
    cin >> a >> b;

    int num = 0;
    if (a <= b)
        for (int i=a; i<=b; i++) {
            if (i%5 == 0) num += i;
    }
    else {
        for (int i=b; i<=a; i++) {
            if (i%5 == 0) num += i;
        }
    }
    cout << num;

    return 0;
}