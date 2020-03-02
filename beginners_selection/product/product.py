a, b = map(int, input().split())

# 1≤a, b≤10000
if 1 <= a and b <= 10000:
    ans = a * b

    if ans % 2 == 0:
        print("Even")
    else:
        print("Odd")
