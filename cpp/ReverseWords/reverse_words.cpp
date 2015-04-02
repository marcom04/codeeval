// https://www.codeeval.com/open_challenges/8/

#include <algorithm>
#include <fstream>
#include <iostream>
#include <iterator>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int main (int argc, char* argv[])
{
    ifstream infile(argv[1]);
    string line;
    while (getline(infile, line))
    {
    	if (line.length() == 0)
           continue;

        istringstream iss(line);
        vector<string> words;
        copy(istream_iterator<string>(iss), istream_iterator<string>(), back_inserter<vector<string> >(words));

        vector<string>::const_iterator it = words.end();
        vector<string>::const_iterator begin = words.begin();
        for (; it-- != begin;)
        {
        	cout << *it;
        	cout << ((it == begin) ? "\n" : " "); 
        }        
    }
    return 0;
}
