def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:  # Sorting in decreasing order
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

if __name__ == "__main__":
    sample_array = [12, 11, 13, 5, 6]
    insertion_sort(sample_array)
    
    # Assertion to check if the array is sorted in decreasing order
    assert sample_array == [13, 12, 11, 6, 5], f"Expected [13, 12, 11, 6, 5], but got {sample_array}"

    # Test cases with assertions
    test_cases = [
        ([5, 2, 9, 1], [9, 5, 2, 1]),     # Expected result after sorting
        ([3, 0, -1, 2], [3, 2, 0, -1]),
        ([7, 8, 9, 10], [10, 9, 8, 7]),
        ([1, 1, 1, 1], [1, 1, 1, 1])
    ]

    for i, (input_arr, expected) in enumerate(test_cases):
        insertion_sort(input_arr)
        # Assertion to validate the sorting result
        assert input_arr == list(expected), f"Test case {i+1} failed: expected {list(expected)}, but got {input_arr}"

    print("All test cases passed!")
