def selection_sort(
    array: list
) -> list:
    '''
    This function sorts a given array and return the sorted array.
    It uses Selection sort of time complexity O(n) and space complexity is O(1),
    as it is an inplace sort algorithm.
    '''

    for i in range(len(array)-1):
        mini = i
        for j in range(i, len(array)):
            if (array[j] < array[mini]):
                mini = j
        array[i], array[mini] = array[mini], array[i]

    return array


if __name__ == "__main__":
    array = list(map(int, input("Enter the elements: ").split()))
    print(f"Un-sorted array is {array}")

    sorted_array = selection_sort(array)
    print(f"Sorted array is {sorted_array}")
