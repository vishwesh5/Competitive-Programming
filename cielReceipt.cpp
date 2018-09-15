/*
 * problem link: https://www.codechef.com/problems/CIELRCPT
 */

#include <iostream>
#include <cmath>

using namespace std;

int pow2 (int N)
{
        return int(log2(N));
}

int main()
{
        int N,T,power,count;
        cin >> T;
        for (int i=0; i < T; i++)
        {
                cin >> N;
                count=0;
                do {
                        power = pow2(N);
                        if (power > 11) power = 11;
                        N = N - pow(2,power);
                        count++;
                } while (N != 0);
                cout << count << "\n";
        }
        return 0;
}
