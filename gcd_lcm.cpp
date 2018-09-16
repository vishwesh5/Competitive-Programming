/*
 * problem link: https://www.codechef.com/problems/FLOW016
 */

#include <iostream>

using namespace std;

int hcf(int a, int b)
{
        int t;
        while (b!=0)
        {
                t = b;
                b = a%b;
                a = t;
        }
        return a;
}

int main()
{
	int T;
	long long product,lcm_val,A,B,hcf_val;
	cin >> T;
	for (int i=0; i<T; i++)
	{
		cin >> A >> B;
		hcf_val = hcf(A,B);
		product = (A*B);
		lcm_val = product/hcf_val;
		cout << hcf_val << " " << lcm_val << "\n";
	}
}
