# "Unique Target Sum Combinations with Frequency Constraints" done by Copilot


# "Finding Unique Combinations That Sum to a Target with Element Frequency Constraints"

# This title captures the essence of the problem:

# "Unique Combinations": Emphasizes that the solution looks for non-duplicate combinations.

# "Sum to a Target": Clearly states the goal of the combinations.

# "Element Frequency Constraints": Highlights the important condition that each element can only be used as many times as it appears in the input list.


# It was definitely a nuanced and thoughtful question — not necessarily “difficult” in the sense of raw complexity, but tricky because it combines multiple constraints that many algorithms overlook:

#     You weren’t just asking for combinations that sum to a target — that’s a classic problem.

#     You added frequency constraints, which means each number can only be used as often as it appears. That’s where most solutions break down.

#     You also wanted unique combinations, not permutations, and no duplicates.

#     And you layered in real-world testing: random inputs, edge cases, and validation.

from collections import Counter
from typing import List

def combination_sum_with_constraints(nums: List[int], target: int) -> List[List[int]]:
    result = []
    original_counter = Counter(nums)
    unique_nums = sorted(original_counter.keys())

    def backtrack(start: int, path: List[int], remaining: int, counter: Counter):
        if remaining == 0:
            result.append(path[:])
            return
        if remaining < 0:
            return

        for i in range(start, len(unique_nums)):
            num = unique_nums[i]
            if counter[num] == 0:
                continue
            new_counter = counter.copy()
            new_counter[num] -= 1
            path.append(num)
            backtrack(i, path, remaining - num, new_counter)
            path.pop()

    backtrack(0, [], target, original_counter)
    return result

nums = [
    113, 227, 341, 459, 113, 227, 341, 571, 683, 797,
    911, 235, 349, 459, 577, 691, 805, 113, 227, 347,
    461, 575, 689, 803, 917, 129, 243, 357, 471, 583
]
target = 1369  # Not a multiple of 10

print("Test Input:")
print("Numbers:", sorted(nums))
print("Target Sum:", target)
print("\nValid Combinations:")

combinations = combination_sum_with_constraints(nums, target)
if combinations:
    for combo in combinations:
        print(combo)
else:
    print("No valid combinations found.")
