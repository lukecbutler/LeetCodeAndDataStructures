#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>
#include <vector>
#include <cmath>
using namespace std;

//logic: 
// 1. if number is negative, flip to positive -> 
// 2. square the number -> 
// 3. append the squared number to the array -> 
// 4. sort the array
// 5. return the array


vector<int> sortedSquares(vector<int>& nums) {

    vector<int> squares = {};

    for (int number : nums) {
            squares.push_back(number * number);
    }

    sort(begin(squares), end(squares)); // sort after the all numbers have been added to squares
    return squares; // return the array 
}


int main(){
    vector<int> nums = {-4,-1,0,3,10};

    vector<int> result = sortedSquares(nums);

    for (int num : result){
        cout << num << " ";
    }

    cout << endl;
    return 0;
}