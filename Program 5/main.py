def print_multiples_of_three(n, multiple=3):
    if multiple < n:
        print(multiple)
        print_multiples_of_three(n, multiple+3)

def print_odd_numbers(n1, n2):
    if n1 <= n2:
        if n1 % 2 != 0:
            print(n1)
        print_odd_numbers(n1 + 1, n2)

print("Multiples of 3: ")
print_multiples_of_three(100)
print(" ")
print("Odd Numbers: ")
print_odd_numbers(10, 50)
