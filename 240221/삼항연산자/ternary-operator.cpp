#include <iostream>
#include <string>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;
    
    int score;
    cin >> score;

    string res = "";


    // 방법1
    // score == 100 ? res = "pass" : res = "failure";
    // cout << res;

    // 방법2
    // res = score == 100 ? res = "pass" : res = "failure";
    // cout << res;

    //방법3
    score == 100 ? cout << "pass" : cout << "failure";

    return 0;
}