def quick_sort(arr):
    """
    Sorts an array in ascending order using the quick sort algorithm.
    :param arr: List of elements to be sorted
    :return: Sorted list
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    sample_array = [22, 7, 6, 8, 1, 4, 5]
    print("Original array:", sample_array)
    sorted_array = quick_sort(sample_array)
    print("Sorted array:", sorted_array)
