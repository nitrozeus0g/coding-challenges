#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <sstream>
using namespace std;

// Class

struct Student {
    private:
        int age, standard;
        string first_name, last_name;
    public:
        void set_age(int a) {age = a;}
        void set_first_name(string f) {first_name = f;}
        void set_last_name(string l) {last_name = l;}
        void set_standard(int s) {standard = s;}
        int get_age() {return age;}
        int get_standard() {return standard;}
        string get_first_name() {return first_name;}
        string get_last_name() {return last_name;}
        string to_string(){
            std::stringstream ss;
            ss << age << "," << first_name << "," << last_name << "," << standard;
            return ss.str();
        }
};

int main() {
    int age, standard;
    string first_name, last_name;
    std::cin >> age >> first_name >> last_name >> standard;
    Student x;
    x.set_age(age);
    x.set_first_name(first_name);
    x.set_last_name(last_name);
    x.set_standard(standard);
    std::cout << x.get_age() << std::endl;
    std::cout << x.get_last_name() << ", " <<  x.get_first_name() << std::endl;
    std::cout << x.get_standard() << std::endl;
    std::cout << std::endl;
    std::cout << x.to_string() << std::endl;
    return 0;
}

