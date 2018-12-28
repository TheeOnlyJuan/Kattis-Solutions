#include<string>
#include<iostream> 
#include <map> 
using namespace std;
int main()
{
	
	while (true) {
		long p1, p2, count = 0,c = 0, d = 0;;
		cin >> p1;
		cin >> p2;
		if (p1 == 0) {
			break;
		}
		long temp;
		long cd1[1000000] = { 0 };
		long cd2[1000000] = { 0 };

		for (long i = 0; i < p1; i++) {
			cin >> temp;
			cd1[i] = temp;
		}
		for (long i = 0; i < p2; i++) {
			cin >> temp;
			cd2[i] = temp;
		}
		
		while (c < p1 && d < p2) {
			if (cd1[c] == cd2[d]) {
				count++;
				c++;
				d++;
			}
			else if (cd1[c] < cd2[d]) {
				c++;
			}
			else {
				d++;
			}
		}
		cout << count<< endl;
	}

	return 0;
}