#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int a, b;
    cin >> a >> b;

    int total = 0; float avg; int number = 0;
    for (int i=a; i<=b; i++) {
        if (i%5 == 0 || i%7 == 0) {
            total += i;
            number++;
        }
    }

    cout << fixed;
    cout.precision(1);
    avg = total / float(number);
    cout << total << " " << avg;

    return 0;
}