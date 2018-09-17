/*
 * problem link: https://www.codechef.com/problems/FCTRL
 */

#include <iostream>
#include <cmath>

using namespace std;

void getTrailingZeros(unsigned int n)
{
	unsigned int i=1,tmp;
	unsigned int totalZeros=0;
	while (1)
	{
		tmp=floor(n/pow(5,i));
		if (tmp > 0)
		{
			totalZeros+=tmp;
			i++;
		}
		else
			break;
	}
	cout << totalZeros << "\n";
}

int main()
{
	int T;
	unsigned int n;
	cin >> T;
	for (int i=0; i<T; i++)
	{
		cin >> n;
		getTrailingZeros(n);
	}
}
