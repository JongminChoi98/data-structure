# LeetCode: 217. Contains Duplicate


class Solution:
    # Create a hashset & compare length
    # Time complexity: O(n)
    # Space complexity: O(n)
    def containsDuplicate_1(self, nums: list[int]) -> bool:
        num_sets = set(nums)
        if len(num_sets) == len(nums):
            return False
        else:
            return True

    # Creating a hashset
    # Time complexity: O(n)
    # Space complexity: O(n)
    def containsDuplicate_2(self, nums: list[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

    # Sort & Compare elements
    # Time complexity: O(nlogn)
    def containsDuplicate_3(self, nums: list[int]) -> bool:
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False


"""
Test case
[1,2,3,1] # True
[1,2,3,4] # False
[1,1,1,3,3,4,3,2,4,2] # True
"""

test_runner = Solution()
print("Solution 1", end=" ")
print(test_runner.containsDuplicate_1([1, 2, 3, 1]), end=" ")
print(test_runner.containsDuplicate_1([1, 2, 3, 4]), end=" ")
print(test_runner.containsDuplicate_1([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
print("Solution 2", end=" ")
print(test_runner.containsDuplicate_2([1, 2, 3, 1]), end=" ")
print(test_runner.containsDuplicate_2([1, 2, 3, 4]), end=" ")
print(test_runner.containsDuplicate_2([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
print("Solution 3", end=" ")
print(test_runner.containsDuplicate_3([1, 2, 3, 1]), end=" ")
print(test_runner.containsDuplicate_3([1, 2, 3, 4]), end=" ")
print(test_runner.containsDuplicate_3([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
