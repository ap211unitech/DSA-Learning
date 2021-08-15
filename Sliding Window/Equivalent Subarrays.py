
# PROBLEM - https://www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/hashmap-and-heaps/equivalent-subarrays-official/ojquestion

n = int(input())
arr = list(map(int, input().split()))

k = len(set(arr))

res = 0
i = 0
j = 0
freq = {}

while(j < n and i < n):
    curr = arr[j]
    freq[curr] = freq.get(curr, 0)+1

    if len(freq) == k:
        res += n-j

        while(len(freq) == k):
            freq[arr[i]] -= 1
            if freq[arr[i]] == 0:
                del freq[arr[i]]
            if len(freq) == k:
                res += n-j
            i += 1

    j += 1
print(res)
