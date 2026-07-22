"""
33. Search in Rotated Sorted Array
LeetCode #33  |  https://leetcode.com/problems/search-in-rotated-sorted-array/
Difficulty: Medium

Approach: <one line on the key idea>
Time:  O(log(n))
Space: O(1)
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if target == nums[m]:
                return m

            if nums[l] <= nums[m]:      #left sorted
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1 
            else: # nums[m] <= nums[r] #right sorted
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1


if __name__ == "__main__":
    s = Solution()
    # quick sanity checks
    # assert s.solve(...) == expected
    print("ok")
