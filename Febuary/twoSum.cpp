/*
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
*/

#include <iostream>
#include <vector>
#include <string>
using namespace std;


vector<int> twoSum(vector<int>& nums, int target) {
    vector<int> indices = {};

    

    return indices;
}

int main(){
    vector<int> nums = {2,7,11,15}; 
    int target = 9;

    vector<int> result = twoSum(nums, target);

    for (int num : result){
        cout << num << " ";
    }

    cout << endl;


    return 0;
}