#include <bits/stdc++.h>
using namespace std;

int main(){
    int N,M;
    string s;
    map<string, int> mp;
    cin >> N;
    for(int i=0; i<N;i++){
        cin >> s;
        auto itr = mp.find(s);
        if(itr == mp.end()){
            mp[s] = 1;
        }else{
            mp[s]++;
        }
    }

    cin >> M;
    for(int i=0; i<M;i++){
        cin >> s;
        auto itr = mp.find(s);
        if(itr == mp.end()){
            mp[s] = -1;
        }else{
            mp[s]--;
        }
    }
    int max = 0;
    for(auto itr = mp.begin(); itr != mp.end(); ++itr) {
        if(itr->second > max){
            max = itr->second;
        }
    }

    cout << max << endl;

}
