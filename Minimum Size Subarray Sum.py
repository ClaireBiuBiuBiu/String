'''
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
'''

#Below two pointer method, since we need to move left part to achieve accumulate goal
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        sum_ = 0
        left = 0
        ans = float('inf')

        for i in range(len(nums)):
            sum_ = nums[i]

            while sum_>=s:
                ans = min(ans,i+1-left)
                sum_ -= nums[left]
                left += 1
        return 0 if ans == float('inf') else ans