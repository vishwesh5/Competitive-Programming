/*
 * Problem link: https://www.codechef.com/LTIME63B/problems/EID
 */

#include <bits/stdc++.h>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

unsigned diff(vector<unsigned int> array)
{
	sort(array.begin(),array.end());

	unsigned int minDiff = INT_MAX;
	
	for (unsigned int i=0; i<array.size()-1; i++)
		if (array.at(i+1) - array.at(i) < minDiff)
			minDiff = array.at(i+1) - array.at(i);
	return minDiff;
}

int main()
{
	unsigned int T,N,tmp;
	vector<unsigned int> coins;
	cin >> T;
	for (unsigned int i=0; i<T; i++)
	{
		coins={};
		cin >> N;
		for (unsigned int j=0; j<N; j++)
		{
			cin >> tmp;
			coins.push_back(tmp);
		}
		cout << diff(coins) << "\n";
	}
}
