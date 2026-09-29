"""
Problem: Aggressive Cows
Category: Searching & Sorting
Pattern: Binary Search on Answer

Time Complexity:  O(N log N + N log(max_dist)) where N is number of stalls
Space Complexity: O(1) auxiliary space (in-place sort)
"""


def largest_min_distance(t, test_cases):
    results = []

    for _ in range(t):
        n, c = test_cases[_][:2]
        stall_location = test_cases[_][2]
        stall_location.sort()

        start = 1
        end = 10**9
        ans = 0

        while start <= end:
            mid = (start + end) // 2
            cow = 1
            prev = stall_location[0]

            for i in range(1, n):
                if stall_location[i] - prev >= mid:
                    cow += 1
                    prev = stall_location[i]
                    if cow == c:
                        break

            if cow == c:
                ans = mid
                start = mid + 1
            else:
                end = mid - 1

        results.append(ans)

    return results


if __name__ == "__main__":
    demo_cases = [
        (5, 3, [1, 2, 8, 4, 9]),
    ]
    results = largest_min_distance(len(demo_cases), demo_cases)
    assert results == [3], f"Expected [3], got {results}"
    print(f"Aggressive cows demo passed: {results}")
