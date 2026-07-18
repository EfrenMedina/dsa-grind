"""
853. Car Fleet
LeetCode #853  |  https://leetcode.com/problems/car-fleet/
Difficulty: Easy | Medium | Hard

Approach: <one line on the key idea>
Time:  O(nlog(n))
Space: O(n)
"""


class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        
        result = 0

        sortedCars = sorted(zip(position, speed), reverse=True)

        cycles = []
        for i in range(len(position)):
            cycle = (target - sortedCars[i][0]) / sortedCars[i][1]

            if cycles and cycle > cycles[0]:
                cycles = []
                result += 1
            cycles.append(cycle)
        if cycles:
            result += 1

        return result



if __name__ == "__main__":
    s = Solution()
    # quick sanity checks
    # assert s.solve(...) == expected
    print("ok")
