/*
 * problem link: https://www.codechef.com/problems/GDOG
 */

#include <iostream>

using namespace std;

int main()
{
	int T;
	unsigned int N,K,max_rem,remainder;

	cin >> T;

	for (int i=0; i<T; i++)
	{
		cin >> N >> K;
		max_rem = 0;
		for (unsigned int j=1; j<=K; j++)
		{
			remainder=N%j;
			if (max_rem < remainder)
				max_rem=remainder;
		}
		cout << max_rem << "\n";
	}
}
