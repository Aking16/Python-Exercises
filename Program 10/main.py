def has_same_element(first_array = [], second_array = []):
    for i in first_array:
        for j in second_array:
            if i == j:
                print(i)

has_same_element(["Amir", "Ali", "Reza", 45], ["Mohammad", "Amir", 45])