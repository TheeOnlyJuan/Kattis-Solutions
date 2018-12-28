#include<string>
#include<iostream> 
#include<vector>
#include <algorithm>
using namespace std;
int main()
{
	string line;
	cin >> line;
	vector<char> chars;
	string output;
	
	for (int i = 0; i < line.size(); i++) {
		if( line[i] == '<'){
			chars.pop_back();
		}
		else {
			chars.push_back(line[i]);
		}
	}
	for (int i = 0; i < chars.size(); i++) {
		output += chars[i];
	}
	if (output.size()) {
		cout << output;
	}
	return 0;
}