#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int m;
    cin >> m;

    if (m == 3 || m == 4 || m == 5) cout << "Spring";
    if (m == 6 || m == 7 || m == 8) cout << "Summer";
    if (m == 9 || m == 10 || m == 11) cout << "Fall";
    if (m == 12 || m == 1 || m == 2) cout << "Winter";
    
    return 0;
}