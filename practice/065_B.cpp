#include <bits/stdc++.h>
using namespace std;

int main(){
    int N, i, tmp, count = 0;
    cin >> N;
    vector<int> A(N);
    for(int i=0; i<N; i++){
        cin >> A[i];
        A[i]--;
    }
    i = 0;
    while(A[i] != -1 && i != 1){
        tmp = i;
        i = A[i];
        A[tmp] = -1;
        count++;
    }
    if(i == 1) cout << count << endl;
    else cout << -1 << endl;
}
