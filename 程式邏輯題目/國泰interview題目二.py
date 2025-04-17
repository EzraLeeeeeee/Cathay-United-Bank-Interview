def reorder_digits(s):
    # 過濾出奇數與偶數
    odd_digits = [c for c in s if int(c) % 2 == 1]
    even_digits = [c for c in s if int(c) % 2 == 0]

    # 排序：奇數降冪、偶數升冪
    odd_sorted = sorted(odd_digits, reverse=True)
    even_sorted = sorted(even_digits)

    return ''.join(odd_sorted + even_sorted)

num = input("輸入：")
result = reorder_digits(num)
print("輸出：" + result)