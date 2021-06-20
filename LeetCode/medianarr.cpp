#include<iostream>
#include<bits/stdc++.h>
#include<list>
#include<iterator>
using namespace std;
int main(){

 list<int> l1 = {1, 2, 3};
 list<int> l2 = {4, 5, 6, 7};

 l1.splice(l1.end(), l2);  //splice function is used to append the list to another.

 list<int>:: iterator it;

 for(auto x : l1){
   cout<<x<<endl;
 }

 cout<<"\n";
 // cout<<l1.size()<<endl;

 if(l1.size()%2 == 0){
  
   int i = (int)(l1.size()/2);
   int j = i + 1;

   cout<<i<<" "<<j<<endl;
   it = l1.begin();
   advance(it, i-1);
   double val1 = *it;
   it = l1.begin();
   advance(it, j-1);
   double val2 = *it;

   cout<<val1<<" "<<val2<<endl;

   double ans = double((val1 + val2)/2);

   cout<<ans<<setprecision(2)<<endl;

 }else {
   int i = (int)(l1.size()/2);

   it = l1.begin();
   advance(it, i);

   cout<<*it<<endl;
 }

 return 0;
}
