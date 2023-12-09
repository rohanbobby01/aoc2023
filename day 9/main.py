def dfs(arr):
    if len(set(arr)) == 1:
        return arr[0]

    new_arr = []

    for i in range(1, len(arr)):
        new_arr.append(arr[i] - arr[i - 1])

    return arr[-1] + dfs(new_arr)


with open('input.txt') as file:
    ans1 = 0
    ans2 = 0

    for line in file.readlines():
        inp = [int(x) for x in line.split()]
        ans1 += dfs(inp)
        ans2 += dfs(inp[::-1])

    print(ans1, ans2)