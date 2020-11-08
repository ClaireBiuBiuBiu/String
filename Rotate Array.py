'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # speed up the rotation
        k %= len(nums)# 这里的好处是 用余数 如果k 小于 总长度 就会返回k 如果k 大于总长度 会返回 多出来的部分

        for i in range(k):
            previous = nums[-1]
            for j in range(len(nums)):
                nums[j],previous = previous,nums[j]
#但是超时了！

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        a = [0] * n # 这有一个好处 不需要空集append 直接建立相应位置 数量的 先用0代替的集合
        for i in range(n):
            a[(i + k) % n] = nums[i]

        nums[:] = a