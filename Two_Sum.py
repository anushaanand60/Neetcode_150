class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pair_idx = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in pair_idx:
                return [pair_idx[complement], i]
            pair_idx[num] = i

        return []

if __name__ == "__main__":
    nums_input = input("Enter numbers separated by spaces: ")
    nums = list(map(int, nums_input.strip().split()))
    target = int(input("Enter the target number: "))
    solution = Solution()
    result = solution.twoSum(nums, target)

    if result:
        print("Indices of the numbers that add up to target:", result)
    else:
        print("No two numbers add up to the target.")
