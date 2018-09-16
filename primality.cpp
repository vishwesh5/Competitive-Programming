/*
 * problem link: https://www.codechef.com/problems/PRB01
 */

#include <iostream>
#include <cmath>

using namespace std;

bool checkPrime(int N)
{
	if (N <= 3)
		return true;

	for(int i=2; i < (int) sqrt(N)+1; i++)
		if (N%i==0)
			return false;
	return true;
}

int main()
{
	int T,N;
	cin >> T;
	for (int i=0; i < T; i++)
	{
		cin >> N;
		if (checkPrime(N))
			cout << "yes";
		else
			cout << "no";
		cout << "\n";
	}
}
