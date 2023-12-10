from collections import defaultdict

with open('input.txt') as file:
    mat = file.read().split()
    row, col = len(mat), len(mat[0])
    dr = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
    mapper = defaultdict(list)

    ans1 = 0
    ans2 = 0

    for r in range(row):
        prev = ''
        check = False
        total = 0
        cur_i = False

        for c in range(col):
            if mat[r][c].isdigit():
                prev += mat[r][c]
                for rr, cc in dr:
                    i = r + rr
                    j = c + cc
                    if i < 0 or j < 0 or i == row or j == col:
                        continue

                    if mat[i][j] != '.' and not mat[i][j].isdigit():
                        check = True
                        if mat[i][j] == '*':
                            cur_i = (i, j)


            elif prev and check:
                val = int(prev)
                total += val
                if cur_i:
                    mapper[cur_i].append(val)
                prev = ''
                check = False
                cur_i = False

            else:
                prev = ''
                check = False
                cur_i = False

        if prev and check:
            val = int(prev)
            total += val
            if cur_i:
                mapper[cur_i].append(val)

        ans1 += total

    ratio = [a * b for a, b in filter(lambda x: len(x) == 2, mapper.values())]
    ans2 = sum(ratio)
    print(ans1, ans2)
