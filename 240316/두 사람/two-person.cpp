#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int age1, age2;
    char sex1, sex2;
    cin >> age1 >> sex1 >> age2 >> sex2;

    if ((age1 >= 19 && sex1 == 'M') || (sex2 == 'M' && age2 >= 19)) cout << 1;
    else cout << 0;

    return 0;
}