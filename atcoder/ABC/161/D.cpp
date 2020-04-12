#include <bits/stdc++.h>
using namespace std;

int main(){
    queue<unsigned long int> q;
    unsigned long int x;
    int K, remainder;
    cin >> K;

    for(int i = 1;i < 10;i++) q.push(i);
    
    for(int i = 0;i < K-1;i++){
        x = q.front();
        remainder = x % 10;
        q.pop();
        if(remainder != 0) q.push(10*x+remainder-1);
        q.push(10*x+remainder);
        if(remainder != 9) q.push(10*x+1+remainder);
    }
    cout << q.front() << endl;
}