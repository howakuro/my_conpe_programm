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
void bubbleSort(vector<T> A){
    bool flag = true;
    int count = 0;
    while(flag){
        flag = false;
        for(int j = A.size() - 1;j >= 1;j--){
            if(A[j] < A[j-1]){
                swap(A[j], A[j-1]);
                count++;
                flag = true;
            }
        }
    }
    printList(A);
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