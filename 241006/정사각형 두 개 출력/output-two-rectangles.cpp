#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    for(int i=0; i<2*n; i++) {
        if (i == n) cout << endl;
        for(int j=0; j<n; j++) {
            cout << '*';
        }
        cout << endl;
    }
    return 0;
}