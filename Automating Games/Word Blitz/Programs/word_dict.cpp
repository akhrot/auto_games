#include<bits/stdc++.h>
using namespace std;

set<string> words;

char mat[10][10];
bool visited[10][10];

string curWord;

vector<string> wordsFound;

bool isValid( int x, int y )
{
	if( x<1 || x>4 || y<1 || y>4 )
		return false;
	return !visited[x][y];
}

void findWords( int x, int y, int n )
{
	curWord.push_back(mat[x][y]);
	visited[x][y] = 1;
	
	if( n==1 )
	{
		if( words.find(curWord)!=words.end() )
			wordsFound.push_back(curWord);
	}
	else
	{
		int nx[8] = { x-1, x-1, x-1, x, x, x+1, x+1, x+1 };
		int ny[8] = { y-1, y, y+1, y-1, y+1, y-1, y, y+1 };
		
		for( int i=0;i<8;i++ )
			if( isValid( nx[i], ny[i] ) )
				findWords( nx[i], ny[i], n-1 );
	}
	
	visited[x][y] = 0;
	curWord.pop_back();
}

int main()
{
	string fname = "words.txt";
	
	ifstream fin(fname);
	
	string word;
	
	while( fin>>word )
	{
		transform( word.begin(), word.end(), word.begin(), ::tolower );
		words.insert(word);
	}
	
	for( int i=1;i<=4;i++ )
		for( int j=1;j<=4;j++ )
		{
			cin>>mat[i][j];
			mat[i][j] = tolower(mat[i][j]);
			visited[i][j] = false;
		}
	curWord = "";
	
	int n;
	
	while(true)
	{
		cout<<"Enter length : ";
		cin>>n;
		
		wordsFound.clear();
		for( int i=1;i<=4;i++ )
			for( int j=1;j<=4;j++ )
				findWords( i, j, n );
		
		sort( wordsFound.begin(), wordsFound.end() );
		
		for( int i=0;i<wordsFound.size();i++ )
			cout<<wordsFound[i]<<endl;
		cout<<endl;
	}
	
	return 0;
}
