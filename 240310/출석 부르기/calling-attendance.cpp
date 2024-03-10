#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int num;
    cin >> num;
    
    if (num == 1) cout << "John";
    else if (num == 2) cout << "Tom";
    else if (num == 3) cout << "Paul";
    else cout << "vacancy";
    return 0;
}