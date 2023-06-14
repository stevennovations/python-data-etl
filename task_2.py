# task_2.py

def second_largest(numbers):
    """
    Find the second largest number in a list.

    :param numbers: List of numbers
    :return: The second largest number or None if it doesn't exist
    """
    # Check if the list has less than 2 elements, in which case the second largest doesn't exist
    if len(numbers) < 2:
        return None

    # Initialize the largest and second largest numbers
    largest = second_largest = float('-inf')

    # Iterate through each number in the list
    for number in numbers:
        # Update the largest and second largest numbers
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest and number != largest:
            second_largest = number

    # If second_largest remains as negative infinity, it means there is no second largest number
    if second_largest == float('-inf'):
        return None

    # Return the second largest number
    return second_largest


# Example usage:
numbers_list = [1, 2, 3, 4, 5]
print(second_largest(numbers_list))  # Output: 4
