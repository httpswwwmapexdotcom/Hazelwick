Fname = input("Enter your forename: ")
Lname = input("Enter your surname: ")
age = int(input("Enter your age: "))
continuation = str(input("Do you want to continue? (y/n): "))
answer = input("Do you want to print your name or username: ")


if answer == "name":
  print (Fname.title(), Lname.title())
elif answer == "username":
  print(Lname[0].title() + Fname[0:5].title() + str(age))
else:


# add a loop function that will keep it running and ask if u want to continue