#include <bits/stdc++.h>
using namespace std;

int main(void){
    int N;
    int move_count = 0;
    int max_move = 0;
    int now_height, before_height;
    cin >> N;
    cin >> before_height;
    for(int i = 0;i < N - 1;i++){
        cin >> now_height;
        if(now_height > before_height){
            if(max_move < move_count) max_move = move_count;
            move_count = 0;
        }else{
            move_count++;
        }
        before_height = now_height;
    }
    if(max_move < move_count) max_move = move_count;
    cout << max_move << endl;
    return 0;
}