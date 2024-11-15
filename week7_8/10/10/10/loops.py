# while loops - execute some code while 



# name = input("enter your name")
# #iterativetive loops 
# if name == "":
#     print("You did not enter your name")
#     #Infinite loops 
# else:
#     print(f"Hello {name}")

# age = int(input("enter your age"))

# while age < 0:
#     print("Age can't be negative")
# #     age = int(input)

# food = input("enter a food you like (q to quit)")
# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another food you like (q to quit):")

#     print ("bye")


# num = int (input("Enter a # between 1-10:"))
# while num < 1 or num > 10:
#     print(f"{num}) is not valid")
#     num = int(input("enter a # betweem 1-10:"))
# else:
#               print(f"Your number is {num}")
    


# for x in reversed (range(1, 11,)):
#         print(x)
#         print("HAPPY NEW YEAR")


# for x in range (1, 21):
#     if x == 13:
#         continue  #continue = skip
#     else:
#         print(x) 



# for x in range (1, 21):
#     if x == 13:
#         break  #break = stop
#     else:
#         print(x) 
listofname = 'Mikey, Joey, Tyrique, Luke'
for name in listofname:
 if name == 'Mikey':
    print('Mikey was not found!')
else: 
    print('Mikey as not found!')
    print(name)
list_of_names2 = ['Thanos','Iron Man','Hulk']
#loop through the list_of_names2 and 
#if the name is Ironman skip over it and 
#print out the other names 
for name in list_of_names2:
    if name == "Ironman":
        continue
