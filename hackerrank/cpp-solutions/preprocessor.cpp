#include <bits/stdc++.h>
using namespace std;



#define getdiff(a,b) ((a)-(b))

int main()
{
  int n, i, Z, x;
  vector<int> v;
  cin >> n;
  for (i=0; i<n; i++)
  {
    cin >> x;
    v.push_back(x);
  }
  int max = *max_element(v.begin(), v.end());
  int min = *min_element(v.begin(), v.end());
  Z = getdiff(max,min);
  int Result = Z;
  cout << Result << endl;
  return 0;
}
