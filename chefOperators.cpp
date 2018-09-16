/*
 * problem link: https://www.codechef.com/problems/CHOPRT
 */

#include <iostream>

using namespace std;

int main()
{
	unsigned int T,A,B;

	cin >> T;

	for (unsigned int i=0; i < T; i++)
	{
		cin >> A >> B;
		if (A < B)
			cout << "<";
		else if (A>B)
			cout << ">";
		else
			cout << "=";
		cout << "\n";
	}
}
