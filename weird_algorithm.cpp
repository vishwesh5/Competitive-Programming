/*
Problem link: https://cses.fi/problemset/task/1068
*/

#include <iostream>

using namespace std;

int main()
{
        // input number
        long long n;
        cin >> n;
        while (true)
        {
                cout << n << " ";
                if (n==1)
                        break;
                if (n%2==0)
                        n /= 2;
                else
                        n = n*3 + 1;
        }
        cout << "\n";
        return 0;
}
