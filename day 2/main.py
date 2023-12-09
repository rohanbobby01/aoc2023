from functools import reduce

with open('input.txt') as file:
    ans1 = 0
    ans2 = 0
    counter = {'r': 12, 'g': 13, 'b': 14}

    for s in file.readlines():
        line = s.translate(str.maketrans('', '', ':,;')).replace(' blue', 'b').replace(' red', 'r').replace(' green', 'g')
        line = line.split()
        g_no = int(line[1])
        check = True
        count = {'r': 0, 'g': 0, 'b': 0}

        for item in line[2:]:
            # For part 1
            color, val = item[-1], int(item[:-1])
            if val > counter[color]:
                check = False

            # For part 2
            count[color] = max(count[color], val)

        ans2 += reduce(lambda a, b: a * b, count.values())

        if check:
            ans1 += g_no

    print(ans1, ans2)