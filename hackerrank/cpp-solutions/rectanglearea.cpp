#include <iostream>

using namespace std;
/*
 * Create classes Rectangle and RectangleArea
 */
class Rectangle {
  public:
    int w, h;
    void display() {
      cout << w << " " << h << endl;
    }
};

class RectangleArea : public Rectangle {
  public:
    void read_input() {
      cin >> w >> h;
    }
    void display() {
      cout << w*h << endl;
    }
    
};


int main() {
  RectangleArea arr;
  int w;
  cin >> w ;
  arr[0] = w;
  arr.Rectangle::display();
  arr.display();
  return 0;
}
