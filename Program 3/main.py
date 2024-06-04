def print_pattern(n):
    for rows in range(1, n*2):
        for cols in range(1, n*2):
            val = min(rows, cols, n*2-rows, n*2-cols)
            if (cols == rows or cols == n*2 - rows):
                print(val, end=' ')
            else:
                print(' ', end=' ')
        print()

while True:
    print_pattern(int(input("Please enter your number: ")))
