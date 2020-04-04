#include <bits/stdc++.h>
#include <cstdio> 
using namespace std;

int main(){
    int W, H, x, y, r;
    cin>> W >> H >> x >> y >> r;
    if(x+r<=W && x-r>=0 && y+r<=H && y-r>=0) printf("Yes\n");
    else printf("No\n");
} 