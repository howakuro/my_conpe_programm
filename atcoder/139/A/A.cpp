#include <bits/stdc++.h>
using namespace std;

int main(void){
    string S, T;
    int count = 0;
    cin >> S;
    cin >> T;
    for(int i = 0;i < 3;i++){
        if(S.at(i) == T.at(i)) count++;
    }
    cout << count << endl;
    return 0;
}
