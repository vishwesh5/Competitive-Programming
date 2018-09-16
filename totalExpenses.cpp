/*
 * problem link: https://www.codechef.com/problems/FLOW009
 */

#include <iostream>

using namespace std;

double totalExpenses(unsigned int N, unsigned int P)
{
	if (N > 1000)
		return (double)N*P*0.9;
	else
		return (double)N*P;
}

int main()
{
	unsigned int T, N, P;
	cin >> T;
	for (unsigned int i=0; i<T; i++)
	{
		cin >> N >> P;
		printf("%.6f\n",totalExpenses(N,P));
	}
}
