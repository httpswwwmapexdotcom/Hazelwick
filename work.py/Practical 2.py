age = int(input("Enter your age:"))

if age < 0:
    print("Invalid age")
elif age < 12:
    print ("Ticket price: £5.00")
elif age >= 12 and age <= 17:
    print("Ticket price: 7.00")
elif age > 64:
    print("Ticket price: £6.00")
elif age >= 18 and age <= 64:
    answer = str(input("Do you have a student card (Y/N):"))
    if answer == "y":
        print ("Ticket price: £8.00")
    else:
        print ("Ticket price: £10.00")