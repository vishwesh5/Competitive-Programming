/*
Problem link: https://cses.fi/problemset/task/1070
*/

#include <iostream>

using namespace std;

void evenBeautifulPermutation(int n)
{
        int i;
        for (i=1; i<=n/2;i++)
                cout << 2*i << " ";
        for (i=0; i < n/2; i++)
                cout << 2*i+1 << " ";
}

void oddBeautifulPermutation(int n)
{
        int i;
        for (i=0; i <= n/2; i++)
                cout << 2*i+1 << " ";
        for (i=1; i <= n/2; i++)
                cout << 2*i << " ";
}

int main()
{
        int n;
        cin >> n;
        if (n == 1)
                cout << 1;
        else if (n <= 3)
                cout << "NO SOLUTION";
        else if (n%2==0)
                evenBeautifulPermutation(n);
        else
                oddBeautifulPermutation(n);
}
