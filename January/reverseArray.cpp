#include <iostream>
#include <string>
#include <vector>
using namespace std;


void reverseString(vector<char>& s) {
        
    int left = 0;
    int right = s.size() - 1; // Use s.size for the number of elements
    
    while (left < right){
        char temp = s[left];
        s[left] = s[right];
        s[right] = temp;

        left++;
        right--;
    }
    }


int main() {

    vector<char> s = {'l', 'u', 'k', 'e'}; //include <char> for strict typing on the vector

    reverseString(s);

    // In C++ you cannot cout an entire vector, you must loop through it
    for (char c : s){
        cout << c;
    }
    cout << endl; // ALWAYS flush your buffer

    return 0;
}