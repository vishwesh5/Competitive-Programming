/*
 * Problem link: https://www.codechef.com/problems/HS08TEST
 */

#include <iostream>

using namespace std;

int main()
{
        int amountToWithdraw;
        double initialAccBalance;
        double epsilon = 0.01;

        cin >> amountToWithdraw >> initialAccBalance;

        double totalWithdraw = amountToWithdraw + 0.50;

        if ((totalWithdraw - initialAccBalance >= epsilon) ||
                (amountToWithdraw % 5 != 0))
                printf("%.2f",initialAccBalance);
        else
                printf("%.2f",initialAccBalance-totalWithdraw);
}
