/*
 * @lc app=leetcode id=9 lang=cpp
 *
 * [9] Palindrome Number
 */

// @lc code=start
class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0){
            return false;
        }
        int a[50] = {0}, i = 0;
        while (x > 0){
            i++;
            a[i] = x % 10;
            x /= 10;
        }
        for (int j = 1; j <= i/2; j++){
            if (a[j] != a[i-j+1]){
                return false;
            }
        }
        return true;
    }
};
// @lc code=end

