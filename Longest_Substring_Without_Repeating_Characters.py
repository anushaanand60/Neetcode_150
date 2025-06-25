class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        
        Brute force could be trying every possible substring, checking if it has all   
        unique characters, and keeping track of the max length. But that would be O(n²).
        Let's visualise it anyways.
        
        n = len(s)
        max_length = 0

        for i in range(n):
            seen_chars = set()
            for j in range(i, n):
                if s[j] in seen_chars:
                    break
                seen_chars.add(s[j])
                max_length = max(max_length, j - i + 1)

        return max_length
        
        Now, putting in sliding window concept ->
        Basically, what we can do is take 2 pointers i and j again to maintain a window 
        of a substring that has unique characters. We'll then keep moving the j pointer 
        rightwards to add more characters. If a duplicate is detected, we just need to 
        shrink the window from left by moving the i pointer rightwards until the 
        duplicate is removed. 
        """
        char_index = {}
        n = len(s)
        max_length = 0

        i = 0
        for j in range(n):
            if s[j] in char_index and char_index[s[j]] >= i:
                i = char_index[s[j]] + 1
            char_index[s[j]] = j
            max_length = max(max_length, j - i + 1)
        return max_length

if __name__ == "__main__":
    s = input("Enter the string: ")
    solution = Solution()
    result = solution.lengthOfLongestSubstring(s)
    print("Length of the longest substring without repeating characters:", result)
