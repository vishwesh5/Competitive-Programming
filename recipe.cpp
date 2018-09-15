/*
 * problem link: https://www.codechef.com/problems/RECIPE
 */

#include <iostream>
#include <vector>

using namespace std;

int hcf(int a, int b)
{
	int t;
	while (b!=0)
	{
		t = b;
		b = a%b;
		a = t;
	}
	return a;
}

int main()
{
	int T,N,tmp,hcf_result;
	vector<int> nums;
	cin >> T;
	for (int i=0; i<T; i++)
	{
		nums={};
		cin >> N;
		for (int j=0; j<N; j++)
		{
			cin >> tmp;
			nums.push_back(tmp);
		}
		hcf_result=nums.at(0);
		for (int j=0; j<N-1; j++)
		{
			hcf_result=hcf(hcf_result,nums.at(j+1));
		}
		for (int j=0; j<nums.size();j++)
		{
			cout << nums.at(j)/hcf_result << " ";
		}
		cout << "\n";
	}
}
