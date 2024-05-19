def longest_non_increasing_subsequence(arr):
    n = len(arr)

    dp = [1] * n
    prev = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[j] >= arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

    max_length = max(dp)
    max_index = dp.index(max_length)

    result = []
    while max_index != -1:
        result.append(arr[max_index])
        max_index = prev[max_index]

    result.reverse()

    return result


a = [5, 3, 4, 8, 6, 7, 2, 3, 1]
print(longest_non_increasing_subsequence(a))