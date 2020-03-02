# inputs
n = int(input())

if 1 <= n and n <= 200:
    input_nums = [i for i in map(int, input().split())]
    nums = [input_nums[i] for i in range(n)]

    count = 0
    while True:
        flag = False
        for i in range(n):
            if not (1 <= nums[i] and nums[i] <= 10 ** 9):
                flag = True

            if nums[i] % 2 != 0:
                flag = True

        if flag:
            break

        for i in range(n):
            nums[i] = int(nums[i] / 2)
        count += 1

    print(count)
