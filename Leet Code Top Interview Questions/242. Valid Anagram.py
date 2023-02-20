class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) == len(t):

            check = list(t)

            for i in s:
                if i in check:
                    check.remove(i)
                    continue
                else:
                    return False

            return True

        else:
            return False



ans = Solution()
s = "anagram"
t = "nagaram"
print(ans.isAnagram(s,t))