/*
 * problem link: https://www.codechef.com/problems/FLOW008
 */

#include <iostream>

using namespace std;

int main()
{
	int N,T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		cin >> N;
		if (N < 10)
			cout << "What an obedient servant you are!\n";
		else
			cout << "-1\n";
	}
}
