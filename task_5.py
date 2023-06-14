# task_5.py

def element_wise_sum(arr1, arr2):
    """
    Compute the element-wise sum of two multidimensional arrays.

    :param arr1: First multidimensional array.
    :param arr2: Second multidimensional array.
    :return: A new multidimensional array containing the element-wise sum.
    """
    # Base case: if the inputs are both integers, return their sum
    if isinstance(arr1, int) and isinstance(arr2, int):
        return arr1 + arr2
    
    # Recursive case: if the inputs are lists, iterate through them and recursively compute the sum
    return [element_wise_sum(a, b) for a, b in zip(arr1, arr2)]

# Example usage:
arr1 = [[1, 2], [3, 4], [5, 6]]
arr2 = [[7, 8], [9, 10], [11, 12]]
result = element_wise_sum(arr1, arr2)
print(result)  # Output: [[8, 10], [12, 14], [16, 18]]


