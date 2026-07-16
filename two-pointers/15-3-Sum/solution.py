"""
15. 3Sum
LeetCode #15  |  https://leetcode.com/problems/3sum/
Difficulty: Medium 

Approach: <one line on the key idea>
Time:  O(n^2)
Space: O(n)
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[List[int]]:
        
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            L = i + 1
            R = len(nums) - 1
            while L < R:
                current_sum = nums[i] + nums[L] + nums[R]
                if current_sum < 0:
                    L += 1
                elif current_sum > 0:
                    R -= 1
                else:
                    result.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
        return result


if __name__ == "__main__":
    s = Solution()
    # quick sanity checks
    # assert s.solve(...) == expected
    print("ok")
