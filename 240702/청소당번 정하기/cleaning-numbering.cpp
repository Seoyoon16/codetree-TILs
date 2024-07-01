#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int n;
    int toilet = 0; int corridor = 0; int classroom = 0;
    cin >> n;

    for (int i=1; i<=n; i++) {
        if (i%12 == 0) toilet += 1;
        else if (i%3 == 0) corridor += 1;
        else if (i%2 == 0) classroom += 1;
    }
    cout << classroom << " " << corridor << " " << toilet;

    return 0;
}