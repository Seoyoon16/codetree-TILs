#include <iostream>

int main() {
    using namespace std;
    
    int a, b;
    cin >> a >> b;

    cout << a/b << '.';

    int c = a*10;
    for (int i=0; i<20; i++) {
        cout << c/b;
        c = (c%b)*10;
    }
    return 0;
}

// 3 7
// 30/7 = 4...2 -> 4
// 30%7*10 / 7 = 2...6 -> 2
// ((30%7)*10) % 7 *10 / 7