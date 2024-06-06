def bit_flip(number):
  if(number == '0'):
    return 1
  elif(number == '1'):
    return 0
  else:
    raise ValueError("Invalid bit value")

while True:
  num = int(input("Enter your number: "))

  binary_num = bin(num)[2:]
  print(f"Binary: {binary_num}")

  n = int(input("Enter the index: "))

  if n < 0 or n >= len(binary_num):
          print("Invalid index, please enter a valid index.")
          continue
  
  print(f"Flipped bit of {binary_num[n]}: {bit_flip(binary_num[n])}")