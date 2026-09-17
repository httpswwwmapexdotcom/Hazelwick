name = input("What is your name:")
height = float(input("Enter your height in centimeters:"))
height_m = height/100
height_i = round(height/2.54)
over = height > 180

print("Hi", name.title())
print("You are", height_m ,"m")
print("You are", height_i ,"inches tall")

if over == True:
  print("You are over 180cm")
else:
  print("You are under 180cm")