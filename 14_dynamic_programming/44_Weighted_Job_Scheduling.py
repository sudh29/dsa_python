"""
Problem: Weighted Job Scheduling
Category: Dynamic Programming
Pattern: Sorting + Binary Search + 1D DP

Time Complexity:  O(N log N) - Sorting jobs and binary search for non-overlapping predecessors
Space Complexity: O(N) - 1D DP array for max profit
"""

"""
class Job:

    # Job class which stores profit and deadline.

    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0
"""


class Solution:
    def JobScheduling(self, jobs, n):
        jobs.sort(key=lambda x: x.profit, reverse=True)
        max_deadline = max(job.deadline for job in jobs)
        slot = [-1] * (max_deadline + 1)
        num_jobs = 0
        max_profit = 0
        for job in jobs:
            job_id = job.id
            deadline = job.deadline
            profit = job.profit
            for j in range(min(max_deadline, deadline), 0, -1):
                if slot[j] == -1:
                    slot[j] = job_id
                    num_jobs += 1
                    max_profit += profit
                    break
        return num_jobs, max_profit


class Job:
    """
    Job class which stores profit and deadline.
    """

    def __init__(self, profit=0, deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0


if __name__ == "__main__":
    jobs = [Job(1, 2, 50), Job(3, 5, 20), Job(6, 19, 100), Job(2, 100, 200)]
    print(f"Max profit from weighted jobs: {Solution().maximum_profit(jobs, len(jobs))}")
