# برنامه ای بنویسید که ابتدا عددی را خوانده سپس عدد n را می خواند و nامین بیت عدد خوانده شده را معکوس میکند. یعنی چانانچه این بیت 1 باشد 0 میشود و برعکس

def bitFlip(number):
  if(number == '0'):
    return 1
  elif(number == '1'):
    return 0
  else:
    raise ValueError("Invalid bit value")

while True:
  num = int(input("Enter your number: "))

  binaryNum = bin(num)[2:]
  print(f"Binary: {binaryNum}")

  n = int(input("Enter the index: "))

  if n < 0 or n >= len(binaryNum):
          print("Invalid index, please enter a valid index.")
          continue
  
  print(f"Flipped bit of {binaryNum[n]}: {bitFlip(binaryNum[n])}")