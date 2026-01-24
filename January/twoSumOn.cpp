
//Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

//O(N) solution - linear time

//Input: nums = [2,7,11,15], target = 9
//Output: [0,1]
//Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

vector<int> twoSum(vector<int>& nums, int target){
    unordered_map<int, int> index_map; // hashmap named 'index_map' that uses integers as the key and values

    for(int i = 0 ; i < nums.size() ; i++){
        int current_num = nums[i]; // get the current number by setting nums[i], that is nums[0] would be 2 if 2 is first in list
        int complement = target - current_num; // calculate complement by subtracting current number from complement

        if (index_map.find(complement) != index_map.end()) {
        // This means the complement WAS found in the map
            return {index_map[complement], i};
        }
        else{
            index_map[nums[i]] = i;
        } 


    }

    return {};
}



int main(){

    vector nums = {2,7,11,15};
    int target = 9;

    vector result = twoSum(nums, target);

    cout << result[1] << ',' << result[0] << endl;

    return 0;
}