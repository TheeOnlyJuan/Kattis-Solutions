#include<string>
#include<iostream> 
#include<vector>
#include <algorithm>
using namespace std;
int main()
{
	int n;
	unsigned long int temp;
	cin >> n;
	vector<unsigned long int> nums(n);
	vector<unsigned long int> highestLeft(n,0);
	vector<unsigned long int> lowestRight(n, 0);
	string output;
	cin >> temp;
	nums[0] = temp;
	highestLeft[0] = temp;
	for (int i = 1; i < n; i++) {
		cin >> temp;
		nums[i] = temp;
		if (temp >= highestLeft[i - 1])
			highestLeft[i] = temp;
		else
			highestLeft[i] = highestLeft[i - 1];
	}


	lowestRight[n - 1] = nums[n - 1];
	for (int i = n-2; i >= 0; i--) {
		if (nums[i] < lowestRight[i + 1])
			lowestRight[i] = nums[i];
		else
			lowestRight[i] = lowestRight[i+1];
	}

	int count = 0;
	for (int i = 0; i < n; i++) {
		if (lowestRight[i] == highestLeft[i])
			count++;
	}
	cout << count << endl;

	cin.get();
	cin.get();
	return 0;
}