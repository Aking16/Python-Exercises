def even_digits(n):
    return [int(d) for d in str(n) if int(d) % 2 == 0]

def power_sum(digits):
    return sum(pow(10, d) for d in digits)

number = int(input("Enter a number: "))
even_digits_list = even_digits(number)
print("Even digits:", even_digits_list)
print("Sum of powers of 10:", power_sum(even_digits_list))