/*
 * problem link: https://www.codechef.com/problems/FLOW017
 */

#include <iostream>

using namespace std;

void secondLargest(unsigned int A,
	       unsigned	int B,unsigned int C)
{
	if ((A > B) && (A > C))
	{
		if (B > C)
			cout << B;
		else
			cout << C;
	}
	else if ((C > A) && (C > B))
	{
		if (A > B)
			cout << A;
		else
			cout << B;
	}
	else if (B > A)
	{
		if (A > C)
			cout << A;
		else
			cout << C;
	}
	cout << "\n";
}

int main()
{
	int T;
	unsigned int A,B,C;
	cin >> T;
	for (int i=0; i<T; i++)
	{
		cin >> A >> B >> C;
		secondLargest(A,B,C);
	}
	return 0;
}
