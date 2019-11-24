#include <bits/stdc++.h>
using namespace std;
int main(void){
    int A,B;
    int power_strip = 0;
    int outlet = 1;
    cin >> A >> B;
    while(outlet < B){
        power_strip++;
        outlet += A - 1;
    }
    cout << power_strip << endl;
    return 0;
}