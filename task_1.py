def reverse_string(s, index=0, result=''):
    """
    Reverse a string using recursion.

    :param s: The input string to reverse
    :param index: The current index (used internally for recursion)
    :param result: The result string being built (used internally for recursion)
    :return: The reversed string
    """
    # Base case: if index is equal to the length of the string, return the result
    if index == len(s):
        return result

    # Recursive case: prepend the current character to the result and increment the index
    return reverse_string(s, index + 1, s[index] + result)


# Example usage:
input_string = "hello"
reversed_string = reverse_string(input_string)
print(reversed_string)  # Output: 'olleh'
