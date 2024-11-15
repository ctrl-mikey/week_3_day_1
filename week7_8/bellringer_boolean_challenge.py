########## Exercise 1: Simple conditional
language = input("What's Your favorite programming language? ")

if language == 'Python':
    print("You love Python!")
else:
    print("Different choice.")

########### Exercise 2: Grading System
Grade = int(input("What's your score? "))

if Grade >= 90:
    print("You got an A")
elif Grade >= 80:
    print("You got a B")
elif Grade >= 70:
    print("You got a C")
elif Grade >= 60:
    print("You got a D")
else:
    print("You got an F")

############# Exercise 3: Admin Login
username = "admin"
logged_in = False
user_input = input("Please log in (enter username): ")

if user_input == username:
    logged_in = True
    print("Welcome admin!")
else:
    print("Invalid username, try again")


########### Excercise 4: Object Identity Check 
list1=[1,2,3]
list2=[1,2,3]
print(list1==list2)



