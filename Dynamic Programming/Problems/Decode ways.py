# We have printed strings, in Recusion/Encode String.py
# Let us count them here..

# For any kind of doubt, Refer https://www.youtube.com/watch?v=jFZmBQ569So&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=20

def answer(n):

    if n[0] == "0":
        return 0

    if len(n) == 1:
        return 1

    dp = [0 for i in range(len(n))]
    dp[0] = 1

    for i in range(1, len(n)):
        prev = n[i-1]
        curr = n[i]
        current_number_formed = prev+curr
        if prev == "0" and curr == "0":
            dp[i] = 0
        elif prev == "0" and curr != "0":
            dp[i] = dp[i-1]
        elif prev != "0" and curr == "0":
            if int(current_number_formed) >= 1 and int(current_number_formed) <= 26:
                if i-2 >= 0:
                    dp[i] = dp[i-2]
                else:
                    dp[i] = 1
            else:
                dp[i] = 0
        else:
            if int(current_number_formed) >= 1 and int(current_number_formed) <= 26:
                dp[i] = dp[i-1]
                if i-2 >= 0:
                    dp[i] += dp[i-2]
                else:
                    dp[i] += 1
            else:
                dp[i] = dp[i-1]

    # print(dp)
    return dp[len(n)-1]


n = input()  # Give number as string like 123 etc
print(answer(n))
