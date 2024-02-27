#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int h, w, bmi;
    double res;

    cin >> h >> w;
    res = h / 100.0;

    bmi = w / (res * res);
    cout << bmi << endl;

    if (bmi >= 25) cout << "Obesity";

    return 0;
}