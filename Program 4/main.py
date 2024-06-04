def two_digit_numbers_same_digits():
    for i in range(10, 100):
        if i % 11 == 0:
            print(i)

def three_digit_numbers_middle_zero():
    for i in range(100, 1000):
        if (i // 10) % 10 == 0:
            print(i)
            
def three_digit_numbers_sum_of_first_two_less_than_third():
    for i in range(100, 1000):
        if (i // 100) + ((i // 10) % 10) < (i % 10):
            print(i)

def four_digit_numbers_mirror():
    for i in range(1000, 10000):
        if (i // 1000 == i % 10) and ((i // 100) % 10 == (i // 10) % 10):
            print(i)

print("2 digit numbers with same digits:")
two_digit_numbers_same_digits()
print(" ")
print("3 digit numbers with zero in the middle:")
three_digit_numbers_middle_zero()
print(" ")
print("3 digit numbers that the 1st and 2nd index of it is smaller than the 3rd index:")
three_digit_numbers_sum_of_first_two_less_than_third()
print(" ")
print("4 digit numbers that the 1st and 2nd index is equal to mirror of 3rd and 4th index:")
four_digit_numbers_mirror()
