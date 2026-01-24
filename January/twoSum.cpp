//The Challenge: Given a list nums and a target, 
//find two numbers that add up to the target and return their indices.

// nums = [2, 7, 11], target = 9
// Result: [0, 1] (because nums[0] + nums[1] = 9)
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

// logic for the twoSums algorithm
vector<int> twoSums(vector<int>& nums, int target){
    unordered_map<int, int> frequency_map; // hashmap named 'frequency_map' that uses ints as the key and value

    for(int i = 0 ; i < nums.size() ; i++){ // loop thru nums, the length of nums number of times
        frequency_map[nums[i]] = i;
    }

    for (auto const& [num1, index1] : frequency_map){
        for (auto const& [num2, index2] : frequency_map){
            if (num1 + num2 == target) {
                return {index1, index2};
            }
        }
    }
    return {};
}

int main(){

    vector<int> nums = {2,7,11};
    int target = 9;

    vector<int> result = twoSums(nums, target);

    cout << result[1] << ',' << result[0] << endl;

    return 0;
}