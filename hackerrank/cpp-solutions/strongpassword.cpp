#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'minimumNumber' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. STRING password
 */

int minimumNumber(int n, string password) {
    // Return the minimum number of characters to make the password strong
	string num = "0123456789";
	string low = "abcdefghijklmnopqrstuvwxyz";
	string upp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	string spc = "!@#$%^&*()-+";

	int nc = 0;
	int lc = 0;
	int uc = 0;
	int sc = 0;
	string p = password;
	for (int i=0; i<p.length(); i++){
		if (num.find(p[i]) < upp.length()+1){nc++;}
		if (low.find(p[i]) < low.length()+1){lc++;}
		if (upp.find(p[i]) < upp.length()+1){uc++;}
		if (spc.find(p[i]) < spc.length()+1){sc++;}
	}
	int ret = 0;
	if (nc == 0){ret++;}
	if (lc == 0){ret++;}
	if (uc == 0){ret++;}
	if (sc == 0){ret++;}

	if (6-n > ret){cout << 6-n << endl;}
	else {cout << ret << endl;}
	return 0;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    string password;
    getline(cin, password);

    int answer = minimumNumber(n, password);

    fout << answer << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

