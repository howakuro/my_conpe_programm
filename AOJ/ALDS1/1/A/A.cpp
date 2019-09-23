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
void insertionSort(vector<T> A){
    printList(A);
    for(int i = 1;i < A.size();i++){
        T v = A[i];
        int j = i - 1;
        while(j >= 0 && A[j] > v){
            A[j+1] = A[j];
            j--;
        }
        A[j+1] = v;
        printList(A);
    }
}

int main(){
    int N;
    cin >> N;
    vector<int> A(N);
    for(int i = 0;i < N;i++){
        cin >> A[i];
    }
    insertionSort(A);
    return 0;
}