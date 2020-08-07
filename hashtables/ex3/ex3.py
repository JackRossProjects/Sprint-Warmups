def intersection(arrays):
    '''
    Propmpt: Find the intersection between multiple lists of integers.
    Do not use numpy or sets to solve this; use dict or hashtables, please.
    We're given a list of lists that contain integers:

    [
        [1, 2, 3, 4, 5],
        [12, 7, 2, 9, 1],
        [99, 2, 7, 1,]
    ]

    And we need to compute the intersection, that is, numbers that exist in all lists.
    From the above input, the return value will be:

    [1, 2]

    Because those are the numbers that exist in all the lists.
    (Output can be in any order.)

    Limits:
    here can be up to 10 lists in the list of lists.
    The lists can contain up to roughly 1,000,000 elements each.
    '''

    # Initialize hash table and final array
    cache = {}
    result = []

    # For each row in the array
    for arr in arrays:
        # For each item in a row
        for i in arr:
            # Check if that value is in the cache
            if i not in cache:
                # Set that value in the cache to 1
                cache[i] = 1
            # If the value is already in the cache (appears between lists)
            else:
                # Increment that value in the cache by 1
                cache[i] += 1
    # For each value in the cache
    for i in cache:
        # If a certain value is greater than 1
        if cache[i] > 1:
            # Add that value to the results array
            result.append(i)
    # Return the intersection
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
