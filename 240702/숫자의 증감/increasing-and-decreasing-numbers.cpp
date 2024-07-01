#include <iostream>

int main() {
    using namespace std;

    char c; int n;
    cin >> c >> n;

    if (c == 'A') {
        for (int i=1; i<=n; i++) {
            cout << i << " ";
        }
    }
    else {
       for (int i=n; i>0; i--) {
            cout << i << " ";
        } 
    }
    return 0;
}