#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int sex, age;
    cin >> sex >> age;

    if (sex == 0) {
        if (age >= 19) cout << "MAN";
        else cout << "BOY";
    }
    else {
        if (age >= 19) cout << "WOMAN";
        else cout << "GIRL";   
    }
    
    return 0;
}