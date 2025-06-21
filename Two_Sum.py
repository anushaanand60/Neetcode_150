class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pair_idx = {}  # Dictionary to store number:index pairs

        for i, num in enumerate(nums):
            complement = target - num  # The number we need to find

            if complement in pair_idx:
                # If complement exists, return its index and current index
                return [pair_idx[complement], i]

            # Store the current number and its index in the dictionary
            pair_idx[num] = i

        # If no solution is found
        return []


# Main program with user input
if __name__ == "__main__":
    # Take a list of integers as input
    nums_input = input("Enter numbers separated by spaces: ")
    nums = list(map(int, nums_input.strip().split()))

    # Take the target value as input
    target = int(input("Enter the target number: "))

    solution = Solution()
    result = solution.twoSum(nums, target)

    if result:
        print("Indices of the numbers that add up to target:", result)
    else:
        print("No two numbers add up to the target.")
