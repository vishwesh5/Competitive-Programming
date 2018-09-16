/*
 * problem link: https://www.codechef.com/problems/AMR15A
 */

#include <iostream>

using namespace std;

int main()
{
	int N;
	int weapons;
	int ready=0,not_ready=0;

	cin >> N;

	for (int i=0; i<N; i++)
	{
		cin >> weapons;

		if (weapons%2==0)
			ready++;
		else
			not_ready++;
	}
	if (ready>not_ready)
		cout << "READY FOR BATTLE";
	else
		cout << "NOT READY";
	cout << "\n";
}
