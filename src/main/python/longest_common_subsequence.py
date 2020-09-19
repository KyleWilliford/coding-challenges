# Created by jzhu at 9/18/20
'''
https://en.wikipedia.org/wiki/Longest_common_subsequence_problem#:~:text=The%20longest%20common%20subsequence%20(LCS,(often%20just%20two%20sequences).

For example, consider the sequences (ABCD) and (ACBAD).
They have 5 length-2 common subsequences: (AB), (AC), (AD), (BD), and (CD);
2 length-3 common subsequences: (ABD) and (ACD);
and no longer common subsequences.
So (ABD) and (ACD) are their longest common subsequences.
'''
import numpy as np

class Solution(object):
    def longestCommonSubsequence(self, string1, string2):
        m, n = len(string1), len(string2)
        max_Subseq = np.zeros((m+1, n+1))
        for i in range(1, m+1):
            for j in range(1, n+1):
                if string1[i-1] == string2[j-1]:
                    max_Subseq[i, j] = max_Subseq[i-1, j-1] + 1
                else:
                    max_Subseq[i, j] = max(max_Subseq[i - 1, j], max_Subseq[i, j - 1])
        print(f'Longest Common Subsequence length is {max_Subseq[-1, -1]}')

        lcs = []
        while i > 0:
            while j > 0:
                if max_Subseq[i, j] == max_Subseq[i-1, j-1] + 1:
                    print(f'(i, j) = ({i, j}), string = {string1[i-1]}')
                    lcs = [string1[i-1]] + lcs
                    i = i-1
                    j = j-1
                elif max_Subseq[i, j] == max_Subseq[i, j-1]:
                    j = j-1
                else:
                    i = i-1
                if i <= 0 or j <= 0:
                    break
            if i <= 0 or j <= 0:
                break
        print(f'Longest Common Subsequence is {lcs}')

        return np.max(max_Subseq)

if __name__ == '__main__':
    string1 = 'GAC'
    string2 = 'AGCAT'
    sol = Solution()
    sol.longestCommonSubsequence(string1, string2)