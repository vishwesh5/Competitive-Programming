/*
 * problem link: https://www.codechef.com/problems/FLOW013
 */

#include <iostream>

using namespace std;

int main()
{
	int T, A,B,C;

	cin >> T;

	for (int i=0; i < T; i++)
	{
		cin >> A >> B >> C;

		if (A+B+C==180)
			cout << "YES";
		else
			cout << "NO";
		cout << "\n";
	}
}
