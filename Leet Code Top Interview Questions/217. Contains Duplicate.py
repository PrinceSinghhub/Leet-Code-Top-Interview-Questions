class Solution:
    def containsDuplicate(self, nums):
        # for i in nums:
        #     if nums.count(i)>1:
        #         return True
        # return False

        # opimize code
        Se = set(nums)
        if len(nums) == len(Se):
            return False
        return True

ans = Solution()
nums = [1,2,3,1]
print(ans.containsDuplicate(nums))