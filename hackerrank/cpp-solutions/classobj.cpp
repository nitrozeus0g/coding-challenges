#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

// Classes and Objects
// answer to i is correct
// answer to i2 should be 49

struct Student{
  public:
    int scores[5];
    int total = 0;
    void input(){
      for (int i=0; i<5; i++){
        cin >> scores[i];
        total += scores[i];
      }   
    }   
    int CalculateTotalScore(){
      return total;
    }   
};

int main() {
  int n;
  cin >> n;
  Student *st = new Student[n]; 
  for (int i=0; i<n; i++){
    st[i].input();
  }
  int chk = st[0].CalculateTotalScore();
  int total = 0;
  int ret = 0;
  for (int i=1; i<n; i++){
    total = st[i].CalculateTotalScore();
    if (total > chk){
      ret += 1;
    } 
  }
  cout << ret << endl;
  return 0;
}
