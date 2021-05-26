#include<iostream>
using namespace std;

    

  class digSum {

     public: 
        

        int getSum(int n){


            int sum = 0;
            while(n! = 0){
                sum = sum + n%10;
                n /= 10;

            }

            return sum;

        }


  };

  int main(){

      digSum g;
      int n = 987;
      cout << g.getSum(n);
      return 0;
        


  }


