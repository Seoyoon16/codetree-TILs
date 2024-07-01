#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int N, num;
    cin >> N;

    for (int i=0; i<N; i++) {
        cin >> num;
        if (num%2 != 0 && num%3 == 0) cout << num << endl;
    }

    return 0;
}