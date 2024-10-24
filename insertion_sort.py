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
    sortedArray = [13,12,11,6,5]
    print("is the array sorted in decreasing order:", sample_array == sortedArray)
    print("Sorted array in decreasing order:",sample_array)
