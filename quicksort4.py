import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: arrays with 0 or 1 element are already sorted

    pivot_index = random.randint(0, len(arr) - 1)  # Randomly select a pivot index
    pivot = arr[pivot_index]  # Pivot element
    left = [x for x in arr if x < pivot]  # Elements less than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot

    # Recursively sort left and right subarrays and combine
    return quick_sort(left) + middle + quick_sort(right)

# Example usage
if __name__ == "__main__":
    arr = [22, 7, 6, 8, 1, 4, 5]
    print("Original array:", arr)
    sorted_arr = quick_sort(arr)
    print("Sorted array:", sorted_arr)