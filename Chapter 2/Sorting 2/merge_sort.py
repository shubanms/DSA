def merge(
    array: list,
    left: int,
    mid: int,
    right: int
) -> None:
    """
    This function merges two sorted sub-arrays of the given array.
    :param array: the input array
    :param left: starting index of the first sub-array
    :param mid: ending index of the first sub-array
    :param right: ending index of the second sub-array
    """
    temp = []

    i = left
    j = mid + 1

    # Merge the two sub-arrays into the temp array
    while i <= mid and j <= right:
        if array[i] <= array[j]:
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1

    # Copy the remaining elements from the first sub-array
    while i <= mid:
        temp.append(array[i])
        i += 1

    # Copy the remaining elements from the second sub-array
    while j <= right:
        temp.append(array[j])
        j += 1

    # Copy the sorted elements from the temp array back to the original array
    for i in range(left, right + 1):
        array[i] = temp[i - left]


def merge_sort(
    array: list,
    left: int,
    right: int
) -> None:
    """
    This function sorts the given array using the merge sort algorithm.
    :param array: the input array
    :param left: starting index of the array or sub-array
    :param right: ending index of the array or sub-array
    """
    if left < right:
        mid = (left + right) // 2
        merge_sort(array, left, mid)
        merge_sort(array, mid + 1, right)
        merge(array, left, mid, right)


if __name__ == "__main__":
    array = list(map(int, input("Enter the elements: ").split()))
    print(f"Unsorted array is {array}")

    # Call the merge_sort function with the entire array
    merge_sort(array, 0, len(array) - 1)
    print(f"Sorted array is {array}")
