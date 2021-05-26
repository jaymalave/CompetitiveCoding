#include <iostream>
using namespace std;

int main(){
  int nums[4];
  int target;
  int i,j;
  
  
  int sizeArr =  sizeof(nums)/sizeof(nums[0]);
  
  
  nums = {2, 7, 11, 15};
  
  
  for(i = 0;i < sizeArr;i++){
    for(j = 0;j < sizeArr;j++){
      if(nums[j] = target - nums[i])
      cout<<i + j<<endl;
    }
  }
  
  return 0;
}