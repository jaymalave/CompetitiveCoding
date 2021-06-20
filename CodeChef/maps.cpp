#include<iostream>
#include<map>
using namespace std;

int main(){
  
  
  map<int, int> m1;
  
  m1[1] = 45;
  m1[2] = 25;
  m1[3] = 07;
  
  
  map<int, int> :: iterator itr;
  
  for(itr = m1.begin(); itr != m1.end(); itr++){
    cout<<(*itr).first<<" "<<(*itr).second<<"\n";
  }
  
  cout<<"This was a map";
  return 0;
}