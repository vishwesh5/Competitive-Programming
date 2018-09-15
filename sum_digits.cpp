/*
 * problem link: https://www.codechef.com/problems/FLOW006
 */

#include <iostream>

using namespace std;

int main()
{
        int T, N, index, tmp, sum_digits;
        cin >> T;
        for (int i=0; i < T; i++)
        {
                cin >> N;
                sum_digits=0;
                index=0;
                while (N != 0)
                {
                        sum_digits += N%10;
                        N /= 10;
                }
                cout << sum_digits << "\n";
        }
        return 0;
}
