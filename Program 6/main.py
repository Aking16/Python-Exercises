def merge_two_arrays(first_array = [], second_array = []):
    print("First array: ", first_array)
    print("Second array: ", second_array)
    first_array.extend(second_array)
    print(first_array)

merge_two_arrays(["Amir", "Ali", "Reza"], ["Mohammad", "Amin"])
