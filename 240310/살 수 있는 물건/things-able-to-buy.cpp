#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int n;
    cin >> n;

    if (n >= 3000) cout << "book";
    else if (n >= 1000) cout << "mask";
    else cout << "no";
    return 0;
}