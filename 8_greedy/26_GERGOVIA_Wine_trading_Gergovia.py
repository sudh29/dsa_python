"""
Problem: GERGOVIA - Wine trading in Gergovia
Category: Greedy Algorithms
Pattern: Greedy Prefix Sum / Balance Accumulator

Time Complexity:  O(N) - Single pass over the demands array
Space Complexity: O(1) auxiliary space
"""


def calculate_work_units(N, demands):
    total_work_units = 0
    net_demand = 0

    for demand in demands:
        net_demand += demand
        total_work_units += abs(net_demand)

    return total_work_units


if __name__ == "__main__":
    demo_demands = [5, -4, 1, -3, 1]
    work = calculate_work_units(len(demo_demands), demo_demands)
    assert work == 9, f"Expected 9, got {work}"
    print(f"Wine trading in Gergovia demo passed: {work} units of work")
