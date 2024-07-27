class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        matrix = [[0 for j in range(len(t2) + 1)] for i in range(len(t1) + 1) ]
        
        for i in range(len(t1)-1, -1, -1):
            for j in range(len(t2)-1, -1, -1):
                if t1[i] == t2[j]:
                    matrix[i][j] = 1 + matrix[i+1][j+1]
                else:
                    matrix[i][j] = max(matrix[i][j+1], matrix[i+1][j])
        
        return matrix[0][0]


if __name__ == "__main__":
    text1 = "abcde"
    text2 = "ace" 
    object = Solution()
    print(object.longestCommonSubsequence(text1, text2))