#include<iostream>
#include <cmath>
using namespace std;
int main() {
  int a,b,c;
  cin >> a >> b >> c;
  int d = b*b - 4*a*c;
  if (d==0){
    int root1,root2;
    cout << "Real and Equal" << endl;
    root1 = (-b - sqrt(d))/(2*a);
    cout << root1 << " " << root1 << endl;
  }
  else if (d > 0){
    cout << "Real and Distinct" << endl;
    int root1,root2;
    root1 = (-b - sqrt(d))/(2*a);
    root2 = (-b + sqrt(d))/(2*a);
    cout << root1 << " " << root2 << endl;
  }
  else
    cout << "Imaginary";
  return 0;
}
