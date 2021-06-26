#include<iostream>
using namespace std;

int main(void){

  int n;
  cin>>n;

  while(n--){
    int a, b, x;
    cin>>a>>b>>x;
    int ans = (b-a)/x;
    cout<<ans;
  }
  return 0;
}