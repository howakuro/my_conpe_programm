#include <bits/stdc++.h>
using namespace std;
 
int main(void){
    long long N;
    long long answer;
    cin >> N;
    answer = N * (N-1) / 2;
    cout << answer << endl;
    return 0;
}