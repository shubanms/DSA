def bubble_sort(
    array: list,
    n: int
) -> None:
    
    '''
    This function sorts an array and updates the values in place.
    This uses an recursive method of bubble sort.
    The time complexity is O(N^2) and space is O(N).
    '''

    if(n == 1):
        return
    
    for i in range(n - 1):
        if(array[i] > array[i+1]):
            array[i], array[i+1] = array[i+1], array[i]
        
    bubble_sort(array, n-1)    
    

if __name__ == "__main__":
    array = list(map(int, input("Enter the elements: ").split()))
    print(f"Un-sorted array is {array}")
    
    bubble_sort(array, len(array))
    print(f"Sorted array is {array}")