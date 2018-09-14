/*
 * problem link: https://www.codechef.com/problems/TSORT
 */

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
        unsigned int t;
        unsigned int N;
        vector<unsigned int> array;
        cin >> t;
        for (unsigned int i=0; i < t; i++)
        {
                cin >> N;
                array.push_back(N);
        }
        sort(array.begin(), array.end());
        for (unsigned int i=0; i < array.size(); i++)
        {
                cout << array.at(i) << "\n";
        }
}
