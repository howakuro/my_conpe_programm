#include <bits/stdc++.h>
using namespace std;

int main(){
    int N, get_count = 0;
    cin >> N;
    vector<int> card(N);
    vector<int> player_point(2, 0);
    for(int i = 0;i < N;i++){
        cin >> card[i];
    }
    
    int get_player = 0;
    while(N != get_count){
        int max_i = 0;
        for(int i = 0;i < N;i++){
            max_i = (card[i] > card[max_i]) ? i : max_i;
        }
        player_point[get_player % 2] += card[max_i];
        card[max_i] = 0;
        get_player++;
        get_count++;
    }
    
    cout << player_point[0] - player_point[1] << endl;
    
}
