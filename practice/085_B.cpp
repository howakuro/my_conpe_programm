#include <bits/stdc++.h>
using namespace std;

int main(){
    int N, before=10000, count =0;
    cin >> N;
    vector<int> d(N);
    for(int i=0;i<N;i++){
        cin>>d[i];
    }
    sort(d.begin(), d.end(), greater<int>());
    for(int i=0;i<N;i++){
        if(d[i] < before){
            before = d[i];
            count++;
        }    
    }
    cout << count << endl;
}
