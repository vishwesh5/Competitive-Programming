/*
 * problem link: https://www.codechef.com/problems/FLOW011
 */

#include <iostream>

using namespace std;

void grossSalary(int salary)
{
	double HRA,DA,gross_salary;
	if (salary < 1500)
	{
		HRA=0.1*salary;
		DA=0.9*salary;
	}
	else
	{
		HRA=500;
		DA =0.98*salary;
	}
	gross_salary=salary+HRA+DA;
	printf("%0.2f\n",gross_salary);
}

int main()
{
	int T, salary;
	cin >> T;
	for (int i=0; i<T; i++)
	{
		cin >> salary;
		grossSalary(salary);
	}
}
