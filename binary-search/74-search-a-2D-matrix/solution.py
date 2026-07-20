"""
74. Search a 2D Matrix
LeetCode #<n>  |  https://leetcode.com/problems/search-a-2d-matrix/
Difficulty: Easy | Medium | Hard

Approach: <one line on the key idea>
Time:  O(log(m*n))
Space: O(1)
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top = 0
        bottom = len(matrix) - 1
        m_row = 0

        while top <= bottom:
            m_row = (top + bottom) // 2

            if target < matrix[m_row][0]:
                bottom = m_row - 1
            elif target > matrix[m_row][-1]:
                top = m_row + 1
            else:
                break

        L = 0
        R = len(matrix[0]) - 1

        while L <= R:
            m = (L + R) // 2
            if target < matrix[m_row][m]:
                R = m - 1
            elif target > matrix[m_row][m]:
                L = m + 1
            else: 
                return True
        
        return False


if __name__ == "__main__":
    s = Solution()
    # quick sanity checks
    # assert s.solve(...) == expected
    print("ok")
