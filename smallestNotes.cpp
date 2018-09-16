/*
 * problem link: https://www.codechef.com/problems/FLOW005
 */

#include <iostream>

using namespace std;

int main()
{
	int N,T;

	int denominations[]={100,50,10,5,2,1};

	cin >> T;

	int totalNotes=0;

	for (int i=0; i<T; i++)
	{
		cin >> N;
		totalNotes=0;
		
		for (int j=0; j<7; j++)
		{
			if (N==0)
			{
				break;
			}
			totalNotes += N/denominations[j];
			N = N%denominations[j];
		}
		cout << totalNotes << "\n";
	}
}
