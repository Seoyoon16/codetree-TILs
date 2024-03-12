#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int Am, Ae, Bm, Be;
    cin >> Am >> Ae >> Bm >> Be;

    if (Am > Bm && Ae > Be) cout << 1;
    else cout << 0;
    
    return 0;
}