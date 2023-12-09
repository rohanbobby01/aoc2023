with open('input.txt') as file:
    ans1 = 0
    ans2 = 0

    for s in file.readlines():
        digits1 = []
        digits2 = []

        for i, char in enumerate(s):
            if char.isdigit():
                digits1.append(char)
                digits2.append(char)

            for j, item in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
                if s[i:].startswith(item):
                    digits2.append(str(j + 1))

        ans1 += int(digits1[0] + digits1[-1])
        ans2 += int(digits2[0] + digits2[-1])

    print(ans1, ans2)
