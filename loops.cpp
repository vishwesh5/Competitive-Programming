/*
 * Problem link: https://cses.fi/208/task/B
 */

#include <iostream>

using namespace std;

long long solve(int n) {
    long long x = 0;
    for (int a = 1; a <= n; a++)
        for (int b = a; b <= n; b++)
            for (int c = a; c <= b; c++)
                x++;
    return x;
}

long long optimizedSolve(long long n)
{
	return (long long)(n*(n+1)*(n+2))/6;
}

int main()
{
	long long n;
	cin >> n;
	cout << optimizedSolve(n) << "\n";
}
