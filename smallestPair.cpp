/*
 * problem link: https://www.codechef.com/problems/SMPAIR
 */

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

unsigned int sum_smallest_pair(vector<unsigned int> nums)
{
	sort(nums.begin(),nums.end());
	return nums.at(0)+nums.at(1);
}

int main()
{
	unsigned int T,N,tmp;
	vector<unsigned int> nums;
	cin >> T;
	for (unsigned int i=0; i<T; i++)
	{
		nums={};
		cin >> N;
		for (unsigned int j=0; j<N; j++)
		{
			cin >> tmp;
			nums.push_back(tmp);
		}
		cout << sum_smallest_pair(nums) << "\n";
	}
}
