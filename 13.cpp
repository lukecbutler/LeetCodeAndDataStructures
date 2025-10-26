#include <iostream> // For printing to the console (cout)
#include <string>   // For using the 'string' type
#include <vector>   // Very common for LeETCode problems
#include <map>

// This line avoids having to write std::cout, std::string, etc.
using namespace std;

// -----------------------------------------------------------------
// LEETCODE PROBLEM GOES HERE
// -----------------------------------------------------------------
class Solution {
public:
    //change back to int & return 
    int romanToInt(string s) {
        map<char, int> numeralValues; // init map of roman numerals: key-char('X') ; value-int('10')
        string buffer = " ";

        // map numerals to integer values
        numeralValues['I'] = 1;
        numeralValues['V'] = 5;
        numeralValues['X'] = 10;
        numeralValues['L'] = 50;
        numeralValues['C'] = 100;
        numeralValues['D'] = 500;
        numeralValues['M'] = 1000;
        
        
        int totalValue = 0;
        for (int i = 0; i < s.size(); i++) {
            int currentValue = numeralValues[s[i]];
            
            // 1. Always add the current value
            totalValue += currentValue;

            // 2. Check if we need to make a correction
            if (i > 0) {
                int previousValue = numeralValues[s[i-1]];
                
                if (currentValue > previousValue) {
                    // We're in a subtraction case (like 'IV' or 'CM')
                    // totalValue is currently (prev + curr)
                    // We want it to be (curr - prev)
                    //
                    // To get there, we subtract 'prev' twice.
                    totalValue -= 2 * previousValue;
                }
            }
        }
        
        return totalValue;
    }
};


int main() {
    // 1. Create an instance of your Solution class
    Solution mySolution;

    // 2. Define your test cases
    string test_case_1 = "IV";



    // 3. Call your function and print the results
    cout << "Test Case 1: " << mySolution.romanToInt(test_case_1) << endl;


    return 0; // Indicates successful execution
}