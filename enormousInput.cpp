/*
 * Problem link: https://www.codechef.com/problems/INTEST
 */

#include <iostream>

using namespace std;

int main()
{
        ios::sync_with_stdio(0);
        cin.tie(0);

        long long n,k,i,count=0,t;
        cin >> n >> k;
        for (i=0; i<n; i++)
        {
                cin >> t;
                if (t%k==0)
                        count++;
        }
        cout << count << "\n";
        return 0;
}
