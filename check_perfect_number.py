def Solve(n):
    # Write your code here

    # To store sum of divisors
    sum = 1

    # Find all divisors and add them
    i = 2
    while i * i <= n:
        if n % i == 0:
            sum = sum + i + n / i
        i += 1

    # If sum of divisors is equal to
    # n, then n is a perfect number

    return "YES" if sum == n and n != 1 else "NO"


T = int(input())
for _ in range(T):
    N = int(input())
    out_ = Solve(N)
    print(out_)
