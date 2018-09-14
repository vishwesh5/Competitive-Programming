/*
Problem link: https://cses.fi/problemset/task/1071
*/

#include <iostream>

using namespace std;

long long getNumAtRowCol(long long row, long long col)
{
        if (col % 2 == 0)
                if (row <= col)
                        return (col-1)*(col-1)+row;
                else
                        if (row %2 == 0)
                                return row*row - (col-1);
                        else
                                return (row-1)*(row-1)+col;
        else
                if (row <= col)
                        return col * col - (row-1);
                else
                        if (row % 2 ==0)
                                return row * row - (col-1);
                        else
                                return (row-1)*(row-1)+col;
}

int main(){
        long long n;
        cin >> n;
        long long row, col;
        for (int i = 0; i < n; i++)
        {
                cin >> row >> col;
                cout << getNumAtRowCol(row,col);
                cout << "\n";
        }
}
