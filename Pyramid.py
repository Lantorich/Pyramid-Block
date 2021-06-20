print("Ascend left-aligned pyramid of blocks ")
height = int(input("Enter the numbers of rows: "))

for i in range(height):
  for j in range(0, i):
      print("#", end =" ")
  
print("\n")