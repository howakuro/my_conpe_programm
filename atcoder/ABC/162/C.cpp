#include <bits/stdc++.h>
using namespace std;


int triple_gcd(int a, int b, int c){
    return gcd(gcd(a,b),c);
}

int main(){
    ios::sync_with_stdio(false);
    int N, sum = 0;
    cin >> N;
    for(int a = 1; a < N; a++){
        for(int b = 1; b < N; b++){
            for(int c = 1; c < N; c++){
                sum += triple_gcd(a, b, c);
            }
        }
    }
    cout << sum << endl;
}
