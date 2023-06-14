# task_4.py

def remove_duplicates_with_order(original_list):
    """
    Remove duplicates from a list while preserving the original order of elements.

    :param original_list: The list from which duplicates should be removed.
    :return: A new list with duplicates removed.
    """
    # Keep track of the elements that have been seen
    seen = set()
    
    # List to store the unique elements in the original order
    result = []
    
    # Iterate through each element in the original list
    for item in original_list:
        # If the item has not been seen before, add it to the result list and mark it as seen
        if item not in seen:
            result.append(item)
            seen.add(item)
    
    # Return the list with duplicates removed
    return result


# Example usage:
original_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 5, 8]
print(remove_duplicates_with_order(original_list))  # Output: [1, 2, 3, 4, 5, 6, 7, 8]


