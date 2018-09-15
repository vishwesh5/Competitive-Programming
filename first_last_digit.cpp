/*
 * problem link: https://www.codechef.com/problems/FLOW004
 */

#include <iostream>
#include <cmath>

using namespace std;

int numDigits(int N)
{
        return log10(N)+1;
}

int sumFirstLastDigit(int N)
{
        int firstDigit = N/pow(10,numDigits(N)-1);
        int lastDigit = N%10;
        return firstDigit+lastDigit;
}

int main()
{
        int T,N;
        cin >> T;
        for (int i=0; i<T; i++)
        {
                cin >> N;
                cout << sumFirstLastDigit(N) << "\n";
        }
        return 0;
}
