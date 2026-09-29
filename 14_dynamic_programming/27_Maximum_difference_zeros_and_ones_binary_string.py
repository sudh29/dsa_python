"""
Problem: Maximum Difference of Zeros and Ones in Binary String
Category: Dynamic Programming
Pattern: Kadane's Algorithm on Mapped Values

Time Complexity:  O(N) - Linear scan applying Kadane's algorithm (+1 for 0, -1 for 1)
Space Complexity: O(1) auxiliary space
"""


class Solution:
    def maxSubstring(self, S):
        # 	    # Kadane's Algorithm
        # 		max_sum = float('-inf')
        #         current_sum = 0
        #         for char in S:
        #             value = 1 if char == '0' else -1
        #             current_sum += value
        #             max_sum = max(max_sum,current_sum)
        #             current_sum = 0 if current_sum < 0 else current_sum
        #         return max_sum if max_sum > 0 else -1

        # DP
        n = len(S)
        dp = [0] * n
        dp[0] = 1 if S[0] == "0" else -1
        for i in range(1, n):
            value = 1 if S[i] == "0" else -1
            dp[i] = max(value, dp[i - 1] + value)
        return max(dp) if max(dp) > 0 else -1


if __name__ == "__main__":
    s = "11000010001"
    print(f"Max diff of zeros and ones: {Solution().maxSubstring(s)}")
