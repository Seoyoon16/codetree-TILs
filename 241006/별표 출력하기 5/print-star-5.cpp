#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    for(int i=n; i>0; i--) {
        for(int j=i*i; j>0; j--) { //987 654 321
            cout << '*';
            if(j%i == 1) cout << ' ';
        }
        cout << endl;
    }
    return 0;
}