#include <bits/stdc++.h>
using namespace std;
int main(){
    long int N, W, w, v, answer = 0;

    cin >> N >> W;
    vector<vector<long int>> dp(N + 1,vector<long int>(W + 1));
    for(int i = 0;i < N; i++){
        cin >> w >> v;
        for(int j = 0;j < W;j++){
            if(j+w <= W) dp[i+1][j+w] = max(dp[i+1][j+w], dp[i][j] + v); // 取る場合
            dp[i+1][j] = max(dp[i+1][j], dp[i][j]); // 取らない
        }
    }

    for(int i = 0; i <= W; i++){
        answer = max(answer,dp[N][i]);
    }

    cout << answer << endl;
    return 0;
}
