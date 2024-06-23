def bubble_sort(
    array: list
) -> list:
    """
    This function sorts a list using the bubble sort
    algorithm and returns an array.
    This algorithm has a time complexity of O(n) and space complexity
    of O(n).
    """

    for i in range(len(array)-1):
        for j in range(i, len(array)):
            if (array[j] < array[i]):
                array[i], array[j] = array[j], array[i]

    return array


if __name__ == "__main__":
    array = list(map(int, input("Enter the elements: ").split()))
    print(f"Un-sorted array is {array}")

    sorted_array = bubble_sort(array)
    print(f"Sorted array is {sorted_array}")
