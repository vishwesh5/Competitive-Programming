#include <iostream>
using namespace std;

int main(){
  int num;
  long int sum=0;
  while (sum >= 0)
  {
    cin >> num;
    sum += num;
    if (sum >= 0)
      cout << num << endl;
    else
      break;
  return 0;
}
