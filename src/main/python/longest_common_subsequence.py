# Created by jzhu at 9/18/20
'''
https://en.wikipedia.org/wiki/Longest_common_subsequence_problem

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
        # print(f'Longest Common Subsequence length is {max_Subseq[-1, -1]}')

        lcs = []
        while i > 0 and j > 0 and len(lcs) < max_Subseq[-1, -1]:
            if max_Subseq[i, j] == max_Subseq[i, j-1]:
                j = j-1
            elif max_Subseq[i, j] == max_Subseq[i-1, j]:
                i = i-1
            elif max_Subseq[i, j] == max_Subseq[i-1, j-1] + 1:
                print(f'(i, j) = ({i, j}), string = {string1[i-1], string2[j-1]}')
                lcs = [string1[i-1]] + lcs
                i = i-1
                j = j-1
        # print(f'Longest Common Subsequence is {lcs}')

        return max_Subseq[-1, -1], lcs

if __name__ == '__main__':
    string1 = 'ABCD'
    string2 = 'ACBAD'
    sol = Solution()
    lcs_len, lcs = sol.longestCommonSubsequence(string1, string2)