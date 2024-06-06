def read_list():
    return input("Enter the list (seperate with space): ").split()

try:
    list1 = read_list()
    list2 = read_list()
    
    num_list1 = [int(i) for i in list1]
    num_list2 = [int(i) for i in list2]
    
    result = [a / b for a, b in zip(num_list1, num_list2)]
    print("Answer: ", result)
    
except ValueError:
    print("ValueError: Please enter valid number")
except ZeroDivisionError:
    print("ZeroDivisionError")
