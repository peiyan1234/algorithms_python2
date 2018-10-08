def findmaximum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        if arr[0] <= arr[1]:
            return findmaximum(arr[1:])
        else:
            arr.pop(1)
            return findmaximum(arr)

print findmaximum([1, 2, 10, 4, 3, 1])
