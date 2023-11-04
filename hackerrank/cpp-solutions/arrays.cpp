#include <bits/stdc++.h>
using namespace std;

// arrays

// 1 <= N <= 1000
// 1 <= A <= 10000

int main() {
	int n;
  cin >> n;
  int arr[10000];
  for (int i = 0; i < n; i++)
    cin >> arr[i];
  for (int i = n-1; i <= 0; i--)
    cout << arr[i] << " ";
  return 0;
}

