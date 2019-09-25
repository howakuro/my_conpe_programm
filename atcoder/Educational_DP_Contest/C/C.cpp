#include <bits/stdc++.h>
using namespace std;
int main(){
    int N, answer = 0;
    cin >> N;
    vector<int> happiness(3);
    vector<vector<int>> dp(N + 1, vector<int>(3));
    for(int i = 0;i < N; i++){
        cin >> happiness[0] >> happiness[1] >> happiness[2];
        for(int j = 0;j < 3; j++){     // 前日の行動
            for(int k = 0;k < 3; k++){ // 今日の行動
                if(j == k) continue;
                dp[i+1][k] = max(dp[i+1][k], dp[i][j] + happiness[k]);
            }
        }
    }

    for(int i = 0;i < 3;i++){
        answer = max(answer,dp[N][i]);
    }

    cout << answer << endl;
    return 0;
}