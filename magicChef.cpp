/*
 * Problem link: https://www.codechef.com/SEPT18B/problems/MAGICHF
 */

#include <iostream>

using namespace std;

unsigned int get_X_after_swap(unsigned int A, unsigned int B, unsigned int S){
        if (A==S){
                S = B;
        }
        else if (B==S){
                S = A;
        }
        return S;
}

int main()
{
        int T;
        unsigned int N,X,S;
        unsigned int A,B;
        cin >> T;
        for (int i = 0; i < T; i++)
        {
                cin >> N >> X >> S;
                //cout << N << " " << X << " " << S << "\n";
                for (int j=0; j < S; j++)
                {
                        cin >> A >> B;
                        X = get_X_after_swap(A,B,X);
                }
                cout << X << "\n";
        }
}
