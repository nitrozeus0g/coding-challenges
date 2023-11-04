#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

// variable sized arrays

// a, q
// k #of a's
// i, j

int main() {
  int n, q, k, i, j;
  std::cin >> n >> q;
  int** arr = new int*[n];
  for (int x = 0; x < n; x++){
    std::cin >> k;
    arr[x] = new int[k];
    for (int y = 0; y < k; y++){
    std::cin >> arr[x][y];
    }
  }
  for (int x = 0; x < q; x++){
    std::cin >> i >> j;
    std::cout << arr[i][j] << std::endl;
  }
  return 0;
}

