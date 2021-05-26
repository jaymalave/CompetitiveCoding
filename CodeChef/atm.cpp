#include <iostream>
using namespace std;

int main(){
    int wd;
    float cash;

    cout<<"Enter the cash to withdraw"<<endl;
    cin>>wd;
    
    

    if (wd%5 == 0){
       final =  cash - wd - 0.5;
    }

    elif(wd > cash){
        cout<<"Insufficient funds"<<endl;
    }
       

    else:
      cout<<"Enter the amount in the multiples of 5"<<endl;
}