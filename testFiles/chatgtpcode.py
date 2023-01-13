def furthest_apart(arr):
    # create an array to store the maximum distance between the two players at each index
    distances = [0] * len(arr)

    # initialize the maximum distance at each index to the value at that index
    for i in range(len(arr)):
        distances[i] = arr[i]

    # iterate through the array from left to right
    for i in range(len(arr)):
        # update the maximum distance at each index
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                distances[j] = max(distances[j], distances[i] + 1)

    # find the maximum distance between the two players
    max_distance = 0
    for i in range(len(arr)):
        max_distance = max(max_distance, distances[i])

    # return the index where the maximum distance between the two players occurs
    for i in range(len(arr)):
        if distances[i] == max_distance:
            return i

    # if no index is found, return -1
    return -1


print(furthest_apart([2, 1, 2, 3, 2]))
