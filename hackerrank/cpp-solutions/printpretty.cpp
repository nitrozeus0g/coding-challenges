#include<bits/stdc++.h>
using namespace std;

int main() {
    int t, i;
    double a, b, c;
    cin >> t;
    for (i=0; i<t; i++){
        cin >> a >> b >> c; 
        cout << "0x" << nouppercase << hex << long(a) << endl;
        cout << setfill('_') << setw(15) << right << showpos << fixed << setprecision(2) << b << endl;
        cout << noshowpos << scientific << setprecision(9) << uppercase << c << endl;
    }
    return 0;
}
// inputs 
// 1  
// 100.345 2006.008 2331.41592653498

// Correct outputs
// 0x64
// _______+2006.01
// 2.331415927E+03 


