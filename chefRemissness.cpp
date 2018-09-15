/*
 * Problem link: https://www.codechef.com/problems/REMISS
 */

#include <iostream>

using namespace std;

int main(){
        int T;
        unsigned int A,B;
        cin >> T;
        for (int i = 0; i < T; i++)
        {
                cin >> A >> B;
                if (A > B)
                        cout << A;
                else
                        cout << B;
                cout << " " << A+B << "\n";
        }
        return 0;
}
