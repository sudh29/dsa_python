# User function Template for python3


class Solution:
    ##Complete this function
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self, n):
        # Optimal O(1) bitwise approach
        if n <= 0:
            return False
        return (n & (n - 1)) == 0

    def isPowerofTwo_iterative(self, n):
        # Iterative O(log n) approach
        if n == 1 or n == 2:
            return True
        elif n % 2 == 0:
            x = 1
            while x < n:
                x = x * 2
                if x == n:
                    return True
                if x > n:
                    return False
        return False
