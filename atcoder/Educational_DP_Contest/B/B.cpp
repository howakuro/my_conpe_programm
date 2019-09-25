#include <bits/stdc++.h>
using namespace std;
int main(){
    int N,K;
    cin >> N >> K;
    vector<int> h(N+K,0);
    vector<int> dp(N+K, INT_MAX);
    for(int i = 0;i < N; i++) cin >> h[i];
    dp[0] = 0;
    for(int i = 0;i < N; i++){
        for(int j = 1;j <= K; j++) dp[i+j] = min(dp[i+j], dp[i] + abs(h[i]-h[i+j]));
    }
    cout << dp[N-1] << endl;
    return 0;
}