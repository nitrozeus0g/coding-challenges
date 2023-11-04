#include <bits/stdc++.h>
using namespace std;

// n = num of ints in v
// v = sorted vector
// q = num of queries
// next q lines = query

// output:
// Yes or No and index


int main()
{
  int n, q, x, y, i, pos;
  cin >> n;
  vector<int> v;

  for (i=0; i<n; i++)
  {
    cin >> y;
    v.push_back(y);
  }
  

  sort(v.begin(), v.end());

  cin >> q;
  for (int j=0; j<q; j++)
  {
    cin >> x;
    vector<int>::iterator low;
    low = lower_bound (v.begin(), v.end(), x);
    pos = (low - v.begin());
    if (x == v[pos])
    {
      cout << "Yes " << pos+1 << endl;
    } 
    else
    {
      cout << "No " << pos+1 << endl;
    }

  }

  return 0;
}
