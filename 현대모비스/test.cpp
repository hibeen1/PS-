#include <iostream>
#include <vector>

using namespace std;

int main(int argc, const char * argv[]) {
    vector<int> v1 = {1, 2, 3};
    vector<pair<int, char> > v2;
    int a, b;
    char c, d;
    v1.push_back(5);
    v1.push_back(6);
    for (int i = 0; i < v1.size(); i++) {
        cout << v1[i] << " ";
    }
    cout << endl;

    a = v1.front();
    b = v1.back();
}
    