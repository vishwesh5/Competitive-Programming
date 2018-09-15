/*
 * problem link: https://www.codechef.com/problems/FSQRT
 */

#include <iostream>
#include <cmath>

using namespace std;

int main()
{
        int T,N;
        cin >> T;
        for (int i=0; i < T; i++)
        {
                cin >> N;
                cout << (int)sqrt(N) << "\n";
        }
        return 0;
}
