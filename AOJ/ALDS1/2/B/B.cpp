#include <bits/stdc++.h>
using namespace std;

template <typename T>
void printList(vector<T> &A){
    for(int i = 0;i < A.size();i++){
        cout << A[i];
        if(i != A.size()-1) cout << " ";
    }
    cout << endl;
}

template <typename T>
void selectionSort(vector<T> A){
    int minj;
    int count = 0;
    for(int i = 0;i < A.size();i++){
        minj = i;
        for(int j = i; j < A.size(); j++){
            if(A[j] < A[minj]) minj = j;
        }
        if(A[i] != A[minj]){
            swap(A[i], A[minj]);
            count++;
        }
    }
    printList(A);
    cout << count << endl;
}

int main(){
    int N;
    cin >> N;
    vector<int> A(N);
    for(int i = 0;i < N;i++){
        cin >> A[i];
    }
    selectionSort(A);
    return 0;
}