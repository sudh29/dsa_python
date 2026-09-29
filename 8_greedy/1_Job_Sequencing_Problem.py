"""
Problem: Job Sequencing Problem
Category: Greedy Algorithms
Pattern: Greedy by Profit / Slot Assignment

Time Complexity:  O(N log N + N * max_deadline) - Sorting by profit and linear slot scan
Space Complexity: O(max_deadline) - Time slots array
"""


class Solution:
    # Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self, Jobs, n):
        # Jobs_list = []
        # for i in range(n):
        #     Jobs_list.append([Jobs[i].id,Jobs[i].deadline,Jobs[i].profit])
        sorted_jobs_end_time = sorted(Jobs, key=lambda x: x.profit, reverse=True)
        array = [0] * n
        job_count = 0
        max_profit = 0
        for i in range(n):
            endtime = sorted_jobs_end_time[i].deadline
            for j in range(endtime - 1, -1, -1):
                if array[j] == 0:
                    array[j] = 1
                    job_count += 1
                    max_profit += sorted_jobs_end_time[i].profit
                    break
        return [job_count, max_profit]


class Job:
    """
    Job class which stores profit and deadline.
    """

    def __init__(self, profit=0, deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0


if __name__ == "__main__":
    j1 = Job(50, 2)
    j1.id = 1
    j2 = Job(10, 1)
    j2.id = 2
    j3 = Job(20, 2)
    j3.id = 3
    j4 = Job(30, 1)
    j4.id = 4
    res = Solution().JobScheduling([j1, j2, j3, j4], 4)
    print(f"Jobs scheduled: {res[0]}, Max profit: {res[1]}")
