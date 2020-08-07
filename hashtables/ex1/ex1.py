def get_indices_of_item_weights(weights, length, limit):
    """
    Prompt: Given a package with a weight limit limit
    and a list weights of item weights, implement a
    function get_indices_of_item_weights that finds two
    items whose sum of weights equals the weight limit limit.
    - Your function will return a tuple of integers that has the following form:
    (zero, one)
    where each element represents the item weights of the two packages.
    - The higher valued index should be placed in the zeroth index and the
    smaller index should be placed in the first index.
    - If such a pair doesn’t exist for the given inputs,
    your function should return None.
    - Your solution should run in linear time.
    Example:
    input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
    output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21
    """

    # HINT: If we store each weight's list index as its value, we can then check
    # to see if the hash table contains an entry for limit - weight.
    # If it does, then we've found the two items whose weights sum up to the limit!

    # Initialize hash table
    weights_dict = {}
    # for each weight in weights list
    for weight in weights:
        # if that weight isn't in the hash table
        if weight not in weights_dict:
            # that spot in the hash table will become its pair
            weights_dict[weight] = limit - weight
        # if weight is in hash table
        else:
            # the next spot in the hash table will become its pair
            weights_dict[weight+1] = limit - weight
    for a in weights_dict:
        for b in weights_dict:
            # if 1 weight plus another weight is equal to the limit
            # AND the values are not equal
            if weights_dict[a] + weights_dict[b] == limit:
                if a != b:
                    # The higher valued index should be placed in the zeroth index and
                    # the smaller index should be placed in the first index
                    return(list(weights_dict.keys()).index(b), list(weights_dict.keys()).index(a))
    # If such a pair doesn’t exist for the given inputs,
    else:
        # the function should return None            
        return None