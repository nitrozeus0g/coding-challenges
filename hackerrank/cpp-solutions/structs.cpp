#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

// struct

struct Student {
  int age;
  string first_name;
  string last_name;
  int standard;
} x;

int main() {
  std::cin >> x.age >> x.first_name >> x.last_name
    >> x.standard;
  std::cout << x.age  << " " << x.first_name << " " << x.last_name << " " << x.standard << std::endl;
  return 0;
}


