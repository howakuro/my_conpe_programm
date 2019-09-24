#include <bits/stdc++.h>
using namespace std;

class Card{
    public:
        char soot;
        int number;    
        bool operator<(const Card &c){
            return number < c.number;
        };
        bool operator>(const Card &c) { return number > c.number; }
        bool operator<=(const Card &c) { return number <= c.number; }
        bool operator>=(const Card &c) { return number >= c.number; }
        bool operator==(const Card &c) { return number == c.number && soot == c.soot;}
        bool operator!=(const Card &c) { return !(number == c.number && soot == c.soot);}
};

void printList(vector<Card> &A){
    for(int i = 0;i < A.size();i++){
        cout << A[i].soot << A[i].number;
        if(i != A.size()-1) cout << " ";
    }
    cout << endl;
}

bool checkSameList(vector<Card> &A, vector<Card> &B){
    if(A.size() != B.size()){
        return false;
    }
    for(int i = 0;i < A.size();i++){
        if(A[i] != B[i]) return false;
    }
    return true;
}

template <typename T>
vector<T> selectionSort(vector<T> A){
    int minj;
    for(int i = 0;i < A.size();i++){
        minj = i;
        for(int j = i; j < A.size(); j++){
            if(A[j] < A[minj]) minj = j;
        }
        if(i != minj){
            swap(A[i], A[minj]);
        }
    }
    return A;
}

template <typename T>
vector<T> bubbleSort(vector<T> A){
    bool flag = true;
    while(flag){
        flag = false;
        for(int j = A.size() - 1;j >= 1;j--){
            if(A[j] < A[j-1]){
                swap(A[j], A[j-1]);
                flag = true;
            }
        }
    }
    return A;
}

int main(){
    int N;
    cin >> N;
    string tmp;
    bool checksame;
    vector<Card> A(N);
    vector<Card> B(N);
    for(int i = 0;i < N;i++){
        cin >> tmp;
        A[i].soot = tmp.at(0);
        A[i].number = tmp.at(1) - '0';
    }
    B = bubbleSort(A);
    printList(B);
    cout << "Stable" << endl;
    A = selectionSort(A);
    printList(A);
    checksame = checkSameList(B,A);
    if(checksame){
        cout << "Stable" << endl;
    }else{
        cout << "Not Stable" << endl;
    } 
    return 0;
}