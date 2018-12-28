#include<string>
#include<iostream> 
#include<vector>
#include <algorithm>
using namespace std;

void groupingDFS(int base, int groupNumber, int x, int y);

typedef vector<int> vInt;
vector<vInt> board;
vector<vInt> group;
int r;
int c;
int main()
{
	string output = "";
	int r1, r2, c1, c2, groupNumber = 1;

	cin >> r >> c;
	cin.get();//gets the \n
	board.resize(r);
	group.resize(r);

	for (int i = 0; i < r; i++) {
		group[i] = vector<int>(c, 0);
		for (int j = 0; j < c; j++) {
			
			board[i].push_back(int(cin.get() - '0'));
		}
		cin.get();//gets the \n
	}
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			if (group[i][j] == 0) {
				groupingDFS(board[i][j], groupNumber, i , j);
				groupNumber++;
			}
		}
	}

	int n, binary;

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> r1 >> c1>> r2 >> c2;
		r1--;c1--;r2--;c2--;
		if (group[r1][c1] == group[r2][c2]) {
			if (board[r1][c1])
				output += "decimal\n";
			else
				output += "binary\n";
		}
		else
			output += "neither\n";
	}
	cout << output;

	
	return 0;
}
void groupingDFS(int base, int groupNumber, int x, int y) {
	if (x < 0 || y < 0 || x == r || y == c)
		return;
	if (board[x][y] != base || group[x][y] != 0)
		return;
	group[x][y] = groupNumber;
	groupingDFS(base, groupNumber, x+1, y);//below
	groupingDFS(base, groupNumber, x, y+1);//right
	groupingDFS(base, groupNumber, x-1, y);//down
	groupingDFS(base, groupNumber, x, y-1);//left

}