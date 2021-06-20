#include<iostream>
using namespace std;

int main(){

  signed int num, reversedNum = 0, rem;  //we have to define revNum as it will o/w store a garbage value 

  cout<<"Enter an integer: ";
  cin>>num;

  while(num != 0){
     rem = num%10;
     reversedNum = reversedNum*10 + rem;
     num /= 10;
  }

  cout<<"Reversed number : "<<reversedNum<<endl;
 
  return 0;
}