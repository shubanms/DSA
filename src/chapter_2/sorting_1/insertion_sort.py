def insertion_sort(
    array: list
) -> list:
    '''
    This function takes an array and sorts it using
    the insertion sort algorithm and returns the sorted array.
    This is in time complexity of O(n) and space complexity O(1),
    as it is a inplace sorting algorithm
    '''

    for i in range(len(array)):
        j = i
        while (j > 0 and array[j-1] > array[j]):
            array[j-1], array[j] = array[j], array[j-1]
            j -= 1

    return array


if __name__ == "__main__":
    array = list(map(int, input("Enter the elements: ").split()))
    print(f"Un-sorted array is {array}")

    sorted_array = insertion_sort(array)
    print(f"Sorted array is {sorted_array}")
