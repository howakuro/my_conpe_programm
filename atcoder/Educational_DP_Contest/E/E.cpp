#include <bits/stdc++.h>
using namespace std;
int main(){
    long long int N, W, w, v, answer = 0;
    int MAX_V = 100001;
    cin >> N >> W;
    vector<vector<long long int>> dp(N + 1,vector<long long int>(MAX_V, LLONG_MAX));
    dp[0][0] = 0;
    for(int i = 0;i < N; i++){
        cin >> w >> v;
        for(int j = 0;j < MAX_V;j++){
            if(j+v < MAX_V) dp[i+1][j+v] = min(dp[i+1][j+v], dp[i][j] + w); // 取る場合
            dp[i+1][j] = min(dp[i+1][j], dp[i][j]); // 取らない
        }
    }

    for(int i = 0; i <= W; i++){
        cout << dp[N][i] << " ";
        answer = max(answer,dp[N][i]);
    }

    cout << answer << endl;
    return 0;
}
