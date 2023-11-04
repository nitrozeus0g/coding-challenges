#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

// stringstream

int main() {
    char ss[800000];
    std::cin.getline(ss, 800000);
    char *x;
    x = strtok(ss, ",");
    while (x!=NULL){
        std::cout << x << std::endl;
        x = strtok(NULL, ",");
    }
    return 0;
}
