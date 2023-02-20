class Solution(object):
    def hammingDistance(self, x, y):
        print(bin(x ^ y)[2::])
        return bin(x ^ y).count('1')



ans = Solution()
x = 1
y = 4
print(ans.hammingDistance(x,y))