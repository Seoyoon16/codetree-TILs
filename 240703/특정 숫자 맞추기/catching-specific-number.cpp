#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int n;
    while (true) {
        cin >> n;
        if (n < 25) cout << "Higher" << endl;
        else if (n == 25) {
            cout << "Good";
            break;
        }
        else cout << "Lower" << endl;
    }
    
    return 0;
}