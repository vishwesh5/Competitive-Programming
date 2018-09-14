/*
 * Problem link: https://cses.fi/dt/task/314
 */

#include <iostream>

using namespace std;

int main(){
        long long permutations=1;
        unsigned int n;
        cin >> n;
        unsigned int i;
        long long modConst = 1000000007;
        for (i=0; i < n; i++)
        {
                //cout << permutations << "\n";
                permutations = (permutations*2)%modConst;
        }
        //cout << permutations << "\n";
        permutations = (permutations)%modConst;
        cout << permutations << "\n";
}
