"""
567. Permutation in String
LeetCode #567  |  https://leetcode.com/problems/permutation-string/
Difficulty: Medium

Approach: <one line on the key idea>
Time:  O(n)
Space: O(s1 + s2)
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False

        s1Map = {}
        permutation = {}
        for i in range(len(s1)):
            s1Map[s1[i]] = 1 + s1Map.get(s1[i], 0)
            permutation[s2[i]] = 1 + permutation.get(s2[i], 0)

        if permutation == s1Map:
                return True

        l = 0
        for r in range(len(s1), len(s2)):
            
            permutation[s2[l]] -= 1
            if permutation[s2[l]] == 0:
                del permutation[s2[l]]
            l += 1

            permutation[s2[r]] = 1 + permutation.get(s2[r], 0)

            if permutation == s1Map:
                return True            

        return False
        

if __name__ == "__main__":
    s = Solution()
    # quick sanity checks
    # assert s.solve(...) == expected
    print("ok")
