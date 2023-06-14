# Python Data ETL

This repository contains a collection of tasks and projects involving the extraction, transformation, and loading (ETL) of data using Python.

## Table of Contents

1. [Task 1: Recursive Reverse a String](task_1.py)
2. [Task 2: Second Largest Number in List](task_2.py)
3. [Task 3: Implementing Cache Class](task_3.py)
4. [Task 4: Set and Order](task_4.py)
5. [Task 5: Elementwise Summation of 2 Matrices](task_5.py)
6. [Task 6: Retrieve order of John O'Brien](task_6.sql)
7. [Task 7: Customers who have not placed Orders](task_7.sql)
8. [Task 8: Orders that include iPhone](task_8.sql)
9. [Task 9: Retrieve Customer and total orders using Temporary Table](task_9.sql)
10. [Task 10: Retrieve all orders and product ordered using Right Join](task_10.sql)
11. [Task 11: Sudoku Challenge](task_11.py)
   
## Task 1: Recursive Reverse a String

### Solution


```python
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
```

## Task 2: Second Largest Number in List

### Solution


```python
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

```

## Task 3: Implementing Cache Class

### Solution


```python
# task_3.py


class Cache:
    def __init__(self):
        # Initialize the cache as an empty dictionary
        self.cache = {}

    def set(self, key, value):
        """
        Add or update a key-value pair in the cache.

        :param key: The key to be added or updated.
        :param value: The value to be associated with the key.
        """
        self.cache[key] = value

    def get(self, key):
        """
        Retrieve the value associated with a given key from the cache.

        :param key: The key whose value is to be retrieved.
        :return: The value associated with the key, or None if the key is not found.
        """
        return self.cache.get(key)

    def delete(self, key):
        """
        Remove a key-value pair from the cache.

        :param key: The key to be removed.
        """
        # Use pop to remove the key, and ignore KeyError if the key is not present
        self.cache.pop(key, None)

    def clear(self):
        """
        Clear all key-value pairs from the cache.
        """
        self.cache.clear()


# Example usage:
cache = Cache()
cache.set("name", "John")
print(cache.get("name"))  # Output: 'John'
cache.delete("name")
print(cache.get("name"))  # Output: None
cache.set("age", 30)
print(cache.get("age"))  # Output: 30
cache.clear()
print(cache.get("age"))  # Output: None



```

## Task 4: Set and Order

### Solution


```python
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



```

## Task 5: Elementwise Summation of 2 Matrices

### Solution


```python
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



```

## Task 6: Retrieve order of John O'Brien

### Solution


```sql
SELECT DISTINCT Orders.order_id, Orders.order_date
FROM Customers
JOIN Orders ON Customers.customer_id = Orders.customer_id
JOIN Order_Items ON Orders.order_id = Order_Items.order_id
WHERE Customers.customer_name = 'John O''Brien';

```

## Task 7: Customers who have not placed Orders

### Solution


```sql
SELECT Customers.customer_id, Customers.customer_name
FROM Customers
LEFT JOIN Orders ON Customers.customer_id = Orders.customer_id
WHERE Orders.order_id IS NULL;
```

## Task 8: Orders that include iPhone

### Solution


```sql
SELECT Orders.order_id, Orders.customer_id, Orders.order_date
FROM Orders
JOIN Order_Items ON Orders.order_id = Order_Items.order_id
WHERE Order_Items.product_id IN (SELECT product_id FROM products WHERE product_name = 'iPhone');

```

## Task 9: Retrieve Customer and total orders using Temporary Table

### Solution


```sql
WITH CustomerOrders AS (
    SELECT customer_id, COUNT(*) AS total_orders
    FROM Orders
    GROUP BY customer_id
)
SELECT Customers.customer_name, COALESCE(CustomerOrders.total_orders, 0) AS total_orders
FROM Customers
LEFT JOIN CustomerOrders ON Customers.customer_id = CustomerOrders.customer_id;

```

## Task 10: Retrieve all orders and product ordered using Right Join

### Solution


```sql
SELECT Orders.order_id, Products.product_name, Order_Items.quantity
FROM Orders
JOIN Order_Items ON Orders.order_id = Order_Items.order_id
RIGHT JOIN Products ON Order_Items.product_id = Products.product_id;

```

## Task 11: Sudoku Challenge

### Solution


```python
# task_11.py

from prettytable import PrettyTable

def is_valid(board, row, col, num):
    """
    Check if it's valid to place a number in a specific cell on a Sudoku board.

    This function checks if the given number is already present in the same
    row, column, or 3x3 box.

    :param board: A 9x9 list of lists representing the Sudoku board.
    :param row: Integer representing the row index.
    :param col: Integer representing the column index.
    :param num: Integer, the number to be placed.
    :return: Boolean, True if it's valid to place the number, False otherwise.
    """

    # Check if the number is in the given row or column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check if the number is in the 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True


def solve_sudoku(board):
    """
    Solve a Sudoku puzzle by filling the empty cells.

    Empty cells are denoted by 0. The function uses a backtracking algorithm.

    :param board: A 9x9 list of lists representing the Sudoku board.
    :return: Boolean, True if the Sudoku puzzle is successfully solved, False otherwise.
    """

    # Find an empty position (denoted by 0)
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                # Try numbers from 1 to 9
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num

                        # Recursively try to fill in the rest
                        if solve_sudoku(board):
                            return True

                        # If the recursion failed, reset the cell to 0 and backtrack
                        board[row][col] = 0

                # If no number can be placed, the Sudoku can't be solved
                return False

    # If the entire board is filled, the Sudoku is solved
    return True



def print_sudoku_board(board):
    """
    Prints a given Sudoku board in a formatted table.
    
    The function uses PrettyTable to format the board. Each cell in the board is 
    centered, and horizontal lines are added between rows. Vertical lines are 
    inserted after every 3 columns to demarcate the 3x3 Sudoku boxes.
    
    :param board: A 9x9 list of lists representing the Sudoku board,
                  where 0 represents an empty cell.
    """

    table = PrettyTable()

    # Disable the table headers
    table.header = False

    # Set the alignment to center
    table.align = 'c'

    # Add horizontal lines between rows
    table.hrules = 1

    # Add rows to the table
    for row in board:
        formatted_row = []
        for j, cell in enumerate(row):
            # Adding vertical line after every 3 columns
            if j % 3 == 0 and j > 0:
                formatted_row.append('||')
            formatted_row.append(str(cell) if cell != 0 else ' ')
        table.add_row(formatted_row)

    # Print the table
    print(table)

# Example Sudoku board
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Print the Sudoku board
print_sudoku_board(sudoku_board)

# Solve the Sudoku
if solve_sudoku(sudoku_board):
    
    # Output the solved Sudoku
    for row in sudoku_board:
        print(row)
else:
    print("No solution exists")

# Print the Sudoku board Final output
print_sudoku_board(sudoku_board)
```