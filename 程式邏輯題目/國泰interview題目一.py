def tristar(n):
    if n < 1:
        print("請輸入大於 0 的整數")
        return

    for i in range(1, n + 1):
        spaces = ' ' * (n - i)  # 左側空格，用來讓星星置中
        if i == 1:
            line = '*'
        elif i == n:
            line = '* ' * n
        else:
            inner_spaces = ' ' * (2 * i - 3)  # 中間空心的寬度
            line = '*' + inner_spaces + '*'
        print(spaces + line)

num = int(input("輸入："))
tristar(num)
