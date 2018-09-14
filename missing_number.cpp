/*
Problem link: https://cses.fi/problemset/task/1083
*/

#include <iostream>

using namespace std;

int main()
{
        long long n, sum;
        cin >> n;
        sum = n*(n+1)/2;
        long long sum_num=0;
        int tmp;
        for (int i=0; i<n-1; i++)
        {
                cin >> tmp;
                sum_num = sum_num + tmp;
        }
        cout << sum - sum_num;
}
