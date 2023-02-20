class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n != 0:
            ans += n % 2
            n = n >> 1

        return ans

ans = Solution()
n = 00000000000000000000000000001011
print(ans.hammingWeight(n))