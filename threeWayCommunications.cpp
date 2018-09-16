/*
 * problem link: https://www.codechef.com/problems/COMM3
 */

#include <iostream>
#include <cmath>

using namespace std;

double distance(int x1, int y1, int x2, int y2)
{
	return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}

int main()
{
int T,maxDist,x1,x2,y1,y2,x3,y3;
cin >> T;
for(int i=0; i<T; i++)
{
	cin >> maxDist;
	cin >> x1 >> y1;
	cin >> x2 >> y2;
	cin >> x3 >> y3;
if (
(distance(x1,y1,x2,y2)<=maxDist)&&
(distance(x2,y2,x3,y3)<=maxDist)
)
	cout << "yes";
else if (distance(x1,y1,x3,y3)<=maxDist)
	cout << "yes";
else
	cout << "no";
cout << "\n";
}
}
