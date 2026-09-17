Fname = input("Enter your forename: ")
Lname = input("Enter your surname: ")
age = int(input("Enter your age: "))

answer = input("Do you want to print your name or username: ")
if answer == "name":
 print (Fname.title(), Lname.title())
elif answer == "username":
 print(Lname[0].title() + Fname[0:5].title() + age)
else:
 end()

# add a loop function that will keep it running and ask if u want to continue