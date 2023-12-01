import bisect

def upper_bound(arr, target):
    # Find the lower bound using bisect_left
    index = bisect.bisect_left(arr, target)
    return arr[index] if index < len(arr) else None

def lower_bound(arr, target):
    # Find the upper bound using bisect_right
    index = bisect.bisect_right(arr, target)
    return arr[index - 1] if index > 0 else None

# Example usage:
sorted_list = [1, 2, 3, 5, 5, 7, 8, 10]
value = 6  # Value for which to find lower and upper bounds

lower = lower_bound(sorted_list, value)
upper = upper_bound(sorted_list, value)

if lower is not None:
    print(f"Lower bound for {value}: {lower}")
else:
    print(f"No lower bound found for {value}")

if upper is not None:
    print(f"Upper bound for {value}: {upper}")
else:
    print(f"No upper bound found for {value}")
