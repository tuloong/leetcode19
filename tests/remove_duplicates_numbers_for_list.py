def remove_duplicates_numbers_for_list(numbers):
    unique_numbers = [] # To store the result in order
    seen = set() # To keep track of seen numbers
    for num in numbers:
        if num not in seen:
            unique_numbers.append(num)
            seen.add(num)
    print(f"Original list:{numbers}")
    print(f"Unique list:{unique_numbers}")

if __name__ == "__main__":
    numbers = [1, 5, 2, 8, 1, 3, 5, 9, 2]
    remove_duplicates_numbers_for_list(numbers)