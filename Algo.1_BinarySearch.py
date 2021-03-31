def binarySearch(S, Low, High):
    if Low > High:
        return 0
    else:
        mid = (Low + High) // 2
        if(x == S[mid]):
            return mid
        else:
            # on the left
            if (x < S[mid]):
                return binarySearch(S, Low, mid -1)
            else:
                return binarySearch(S, mid+1, High)


x = 18
S = [1, 2, 5, 7, 9, 11, 15, 18, 21, 28, 32, 46, 57, 69]
loc = binarySearch(S, 0, len(S)-1)

print("x == ", x)
print("the key is in", loc)