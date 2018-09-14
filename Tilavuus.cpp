/*
 * Problem link: https://cses.fi/dt/task/315
 */

#include <iostream>
#include <cmath>

using namespace std;

int main()
{
        double r;
        cin >> r;
        double volume=0;
        volume = 4.0/3.0*3.141593*pow(r,3.0);
        printf("%.8f\n",volume);
//      cout << volume;
}
