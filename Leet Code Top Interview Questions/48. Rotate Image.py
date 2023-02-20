class Solution(object):
    def rotate(self, matrix):

        ans = []

        for i in range(len(matrix)):
            temp = []

            for j in range(len(matrix)):
                temp.append(matrix[j][i])

            temp = temp[::-1]
            ans.append(temp)
        matrix[:] = ans
        return matrix


ans = Solution()
arr = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(ans.rotate(arr))


