#include<bits/stdc++.h>
using namespace std;
static int z=1;
int repeatloop = 0;




void right(long n){
        
        int k;
       int arr[n][n];

       for(int i=n-1; i>=0; i--){
           k=i;
           repeatloop++;
           for(int j=0;j<n && j<repeatloop && k<=n-1;j++,k++){
               arr[k][j] = z;
               z++;
           }
       }

       for(int i=0;i<n;i++){
           for(int j=0;j<n;j++){
               cout<<arr[i][j]<<" ";
           }
           cout<<endl;
       }

    
}

int main(){
    long n;
    
    cin>>n;
    right(n);



    return 0;

}
