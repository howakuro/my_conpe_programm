#include <bits/stdc++.h>
using namespace std;

int main(){
    int N, M, a, b;
    cin >> N >> M;
    vector<int> city(N, 0);
    for(int i = 0; i < M; i++){
        cin >> a >> b;
        city[a-1]++;
        city[b-1]++;
    }
    for(int i = 0; i < N; i++){
        cout << city[i] << endl;
    }
}
