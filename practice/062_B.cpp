#include <bits/stdc++.h>
using namespace std;

int main(){
    int H, W;
    cin >> H >> W;
    vector<char> A(H*W);
    for(int i = 0; i < H; i++){
        for(int j = 0; j < W; j++){
            cin >> A.at(i * W + j); 
        }
    }
    for(int i = 0; i < H + 2; i++){
        for(int j = 0; j < W + 2; j++){
            if(i == 0 || j == 0 || j == W + 1 || i == H + 1){
                cout << "#";
                if(j == W + 1) cout << endl;
            }else{
                cout << A.at( ((i-1) * W) + (j-1) ) ;
            }
        }
    }
}
