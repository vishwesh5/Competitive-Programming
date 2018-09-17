/*
 * problem link: https://www.codechef.com/problems/FLOW014
 */

#include <iostream>

using namespace std;

void grade_steel (int hardness, double carbon, int tensile)
{
	if (hardness > 50)
	{
		if (carbon < 0.7)
		{
			if (tensile > 5600)
				cout << "10\n";
			else
				cout << "9\n";
		}
		else
		{
			if (tensile > 5600)
				cout << "7\n";
			else
				cout << "6\n";
		}
	}
	else
	{
		if (carbon < 0.7)
		{
			if (tensile > 5600)
				cout << "8\n";
			else
				cout << "6\n";
		}
		else
		{
			if (tensile > 5600)
				cout << "6\n";
			else
				cout << "5\n";
		}
	}
}

int main()
{
	int T, hardness, tensile;
	double carbon;
	cin >> T;
	for (int i=0; i<T; i++)
	{
		cin >> hardness >> carbon >> tensile;
		grade_steel(hardness,carbon,tensile);
	}
}
