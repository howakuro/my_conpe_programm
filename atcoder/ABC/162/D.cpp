#include <bits/stdc++.h>
using namespace std;
 

int main(){
    int N, count = 0;
    string S;
    cin >> N;
    cin >> S;
    for(int k = 0;k < N;k++){
        for(int j = 0;j < k;j++){
            for(int i = 0;i < j;i++){
                if(S[i]!=S[j] && S[i]!=S[k] && S[j]!=S[k] && j-i != k-j) count++;
            }
        }
    }
    cout << count << endl;
}