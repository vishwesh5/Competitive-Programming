/*
 * problem link: https://www.codechef.com/problems/HORSES
 */

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void minDiff(vector<unsigned int> horses)
{
	sort(horses.begin(),horses.end());
	unsigned int minDiff = 1000000009;
	unsigned int diff;
	for (int i=0; i< horses.size()-1; i++)
	{
		diff = horses.at(i+1)-horses.at(i);
		if (diff < minDiff)
			minDiff=diff;
	}
	cout << minDiff << "\n";
}

int main()
{
	int T, N;
	unsigned int S;
	vector<unsigned int> horses;
	cin >> T;
	for (int i=0; i<T; i++)
	{
		cin >> N;
		horses={};
		for (int j=0; j<N; j++)
		{
			cin >> S;
			horses.push_back(S);
		}
		minDiff(horses);
	}
}
