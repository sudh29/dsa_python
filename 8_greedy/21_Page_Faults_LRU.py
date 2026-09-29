"""
Problem: Page Faults in LRU Cache
Category: Greedy Algorithms
Pattern: Least Recently Used (LRU) / Simulation

Time Complexity:  O(N * C) where C is cache capacity
Space Complexity: O(C) - Memory frames storage
"""


class Solution:
    def pageFaults(self, N, C, pages):
        arr = []
        page_fault = 0
        for i in range(N):
            page = pages[i]
            if page not in arr:
                if len(arr) == C:
                    arr.pop(0)
                arr.append(page)
                page_fault += 1
            else:
                arr.remove(page)
                arr.append(page)
        return page_fault


if __name__ == "__main__":
    pages = [5, 0, 1, 3, 2, 4, 1, 0, 5]
    c = 4
    print(f"Page faults with capacity {c}: {Solution().pageFaults(len(pages), c, pages)}")
