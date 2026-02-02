//The Challenge: Return true if string is a palindrome
#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>
#include <vector>
using namespace std;

// logic for the twoSums algorithm
bool isPalindrome(string s) {
    if (s.size() == 0 or s.size() == 1){
        return true;
    }

    vector<char> array_of_characters = {}; // create the vector of a new string
    
    transform(s.begin(), s.end(), s.begin(), ::tolower); // transform the string to lowercase

    // Core logic - loop through string 's' and check if each character is a letter or number
    for(int i = 0; i < s.size(); i++){
        if (isalnum(s[i])){ // isalpha checks if letter; isalnum checks if number
            array_of_characters.push_back(s[i]);
        }
    }

    // construct the string, using the array of vectors, from the first index of the vector to the last index of the vector
    string final_string(array_of_characters.begin(), array_of_characters.end());

    string original_final_string = final_string; // make a copy, as reverse a string reverses the actual string in computer memory

    ::reverse(final_string.begin(), final_string.end()); // reverse the original

    // compare the copy and the original
    if (original_final_string == final_string){
        return true;
    }
    else{
        return false;
    }

}


int main(){
    string s = "racecar";

    bool result = isPalindrome(s);

    cout << result;

    cout << endl;
    return 0;
}