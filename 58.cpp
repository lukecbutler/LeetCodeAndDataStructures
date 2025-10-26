/*
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
*/

#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

// LEETCODE PROBLEM GOES HERE
class Solution {
public:
    string lengthOfLastWord(string s) {
        string buffer = "";

        int lastCharacterIndex = s.size()-1; // start at last character
        bool hitCharacterFlag = false; // set the flag for if the backwards for loop as hit a character

        string lastWord = ""; // init the word that will be returned

        for (int i = lastCharacterIndex; i >= 0; i--){ // loop through entire string

            if (s[i] != ' '){ // if letter (starting at back hits a character)
                lastWord += s[i];
                if (s[i-1] == ' '){
                    hitCharacterFlag = true;

                }
                if (hitCharacterFlag == true){
                    cout << lastWord.size();
                }
            }
        }

        cout << lastWord << endl;

        return buffer;
    }
};

int main() {
    // 1. Create an instance of your Solution class
    Solution mySolution;

    // 2. Define your test cases
    string test_case_1 = "Hello World";


    // 3. Call your function and print the results
    cout << "Test Case 1:" << mySolution.lengthOfLastWord(test_case_1) << endl;

    return 0;
}