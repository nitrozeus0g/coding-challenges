#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

/*
	 Virtual Functions

	 Correct Output for input:

	 Walter 56 99 1
	 Jesse 18 403 1
	 Pinkman 22 135 2
	 White 58 87 2
*/
class Person {
	protected:
		string name;
		int age;
	public:
		Person() {}
		virtual void getdata() {}
		virtual void putdata() {}
};
class Professor: public Person {
	private:
		int publications, cur_id;
		static int id;
	public:
		Professor() {cur_id = ++id;}
		void getdata() {cin >> name >> age >> publications;}
		void putdata() {cout << name << " " << age << " " << publications << " " << cur_id << endl;}
};
class Student: public Person {
	private:
		const int max = 6;
		int *marks = new int [max];
	  int	cur_id;
		static int id;
	public:
		int sum = 0;
		Student() {cur_id = ++id;}
		void getdata() {
			cin >> name >> age;
			for(int c=0; c<6; c++) {cin >> marks[c];}
		}
		void putdata() {
			cout << name << " " << age << " ";
			for(int c=0; c<6; c++) {sum += marks[c];}
			cout << sum << " " << cur_id << endl;
		}
};
int Professor::id = 0;
int Student::id = 0;

int main() {
	int n, x;
	cin >> n;
	Person *per[n];
	for(int c=0; c<n; c++) {
		cin >> x;
		if(x==1) {per[c] = new Professor;}
		else {per[c] = new Student;}
		per[c] -> getdata();
	}
	for(int c=0; c<n; c++) {per[c]->putdata();}
	return 0;
}
