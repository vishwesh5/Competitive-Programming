/*
Problem statement: https://cses.fi/210/task/B
*/
#include <iostream>

using namespace std;

int main()
{
        long long A, B;
        cin >> A >> B;
        long long C = 1000000007LL;
        int answer = ((A%C)*(B%C))%C;
        cout << answer;
}
