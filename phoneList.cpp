#include<string>
#include<iostream> 
#include<vector>
#include <algorithm>
using namespace std;
int main()
{
	int cases, conSize;
	cin >> cases;
	vector<string> contacts;
	string temp;
	bool valid;
	for (int i = 0; i < cases; i++) {
		valid = true;
		cin >> conSize;
		contacts.clear();
		for (int x = 0; x < conSize; x++) {
			cin >> temp;
			contacts.push_back(temp);
		}
		sort(contacts.begin(), contacts.end());
		for (int x = 0; x < conSize-1; x++) {
				if (contacts[x] == contacts[x + 1].substr(0, contacts[x].size())) {
					valid = false;
					break;
				}
		}
		if (valid) {
			cout << "YES" << endl;
		}
		else {
			cout << "NO" << endl;
		}
	}

	return 0;
}