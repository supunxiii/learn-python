# basic string concat
#my_goal = "ace the exam"
#subject = "I am gonna "
#sentence = subject + my_goal
#print(sentence)


# ints
# age = 21
# age += 1
# print("i am " + str(age))


# floats
# height = 169.9
# print("my height is " + str(height))


# boolean data
# human = True
# print("i am a human: " + str(human))


#multiple assignment
#name, age, attractive = "supun", 22, True
#print(name)
#print(age)
#print(attractive)


# password
# password = "admin"

# input_password = input("enter password \n")
# if input_password.lower() == password:
    # print("Welcome")
# else:
    # print("try again")


# string methods
# characters = "supun"
# print(len(characters))
# print(characters.capitalize())
# print(characters.upper())
# print(characters.lower())
# print(characters.isdigit())
# print(characters.find("p"))
# print(characters.count("u"))
# print(characters.replace("u", "e"))
# print(characters*6)


# string indexing
# name = "supun seth xiii"
# first_name = name[0:5]
# middle_name = name[6:10]
# last_name = name[11:]
# wtf_name = name[2:11:2]
# reversed_name = name[::-1]
# print(first_name)
# print(middle_name)
# print(last_name)
# print(wtf_name)
# print(reversed_name)


# string slicing
# website_1 = "https://google.com"
# website_2 = "https://dod.gov"
# domain_name = slice(8, -4)         #this will create a SLICE OBJECT!!!
# print(website_1[domain_name])
# print(website_2[domain_name])


# math module
# import math
# pi = 3.14
# x = 1
# y = 2
# z = 6
# print(pi)
# print(round(pi))
# print(abs(pi))
# print(max(x, y, z))
# print(min(x, y, z))
# print(pow(pi, 2))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(math.sqrt(pi))


# memorizing if statements (selection)
# marks =  int(input("enter your marks in proper numbers (NO DECIMALS ALLOWED): \n"))
# if marks == 100:
#     print("congrats! you have scored full marks!")
# elif marks >= 75:
#     print("you've got an A pass")
# elif 75 > marks >= 65:
#     print("you've got a B pass")
# elif 65 > marks >= 45:
#     print("you've got a C pass")
# elif 45 > marks >= 33:
#     print("you've got an S pass")
# elif 33 > marks >= 0:
#     print("you've got a W")
# else:
#     print("sorry! enter a valid mark next time!")


# a brief idea about logical operators (and/or)
# temp = int(input("enter your room temperature: \n"))
# if temp >= 0 and temp <= 35:
#     print("temperature is great! go outside!")
# elif temp < 0 or temp > 35:
#     print("inhabitable temperature! stay inside!")


# a brief idea about logical operators (not)
# temp = int(input("enter your room temperature: \n"))
# if not(temp >= 0 and temp <= 35):
#     print("inhabitable temperature! stay inside!")
# elif not(temp < 0 or temp > 35):
#     print("temperature is great! go outside!")


# a brief idea about logical operators (not)
# ferrari_worth = int(input("enter a ferrari's price: \n"))
# bank_account = int(input("how much you have got in your bitcoin wallet: \n"))
# loan = int(input("how much you willing to be in debt: \n"))
# if ferrari_worth < bank_account or ferrari_worth < loan:
#     print("You can buy a rari! : )")
# if not(ferrari_worth < bank_account or ferrari_worth < loan):
#     print("Sorry come another day to buy a ferrari!")


# using a while loop for a condition
# name = ""
# while len(name) == 0:
#     name = input("enter your name monsieur: \n")
# print("Bonjour " + name)


# using a while loop to sum the nums in a list
# total = 0
# count = 0
# my_list = [13, 6, 611, 999, 13]
# while count < len(my_list):                # instead of len(my_list); 5 can be used as well
#     total = total + my_list[count]
#     count = count + 1
# print("The sum of my_list is " + str(total))


# using a while to output the number of guesses
# color = "red"
# guess = " "
# guesses = 0
# while guess != color:
#     guess = input("What is the color?  \n")
#     guesses += 1
# if guesses == 1:
#     print("You took 1 try and you've guessed it right!")
# else:
#     print("You took this many guesses to guess: " + str(guesses))


# for loops
# for i in range(13):
#     print(i+1)

# for i in range(13, 67):
#     print(i)

# for i in range(13, 66, 3):   # with a third argument as a 'STEP'
#     print(i)

# for i in ("supun seth xiii"):
#     print(i)

#countdown
# import time
# for seconds in range(10, 0, -1):
#     print(seconds)
#     time.sleep(1)     # halts printing each output from the for loop for a second (1 second)
# print("hello world!")



# nested for loops to print a rectangular shape from any keyboard character
# rows = int(input("enter the number of rows: \n"))  # gonna be handled by the outer loop
# columns = int(input("enter the number of columns: \n"))  # gonna be handled by the inner loop
# figure = input("enter any character you like: \n")
# print()
# for i in range(rows):
#     for j in range(columns):
#         print(figure, end="")    # "end" argument will prevent the cursor from going to the next line. if it goes to the next line we won't get a rectangular shape instead it'll be like vertical line of characters.
#     print()



# loop control statements: continue
# phone_number = "666-131-1776"
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")



# loop control statements: break
# while True:     # similar code is in line 128
#     name = input("enter your name: \n")
#     if name != "":
#         print("hi " + name + "!")
#         break



# loop control statements: pass
# for i in range(0, 26):
#     if i == 13:
#         pass    # passing 13 coz it's considered to be an unlucky number by some IDIOTS!
#     else:
#         print(i)



# lists
# favorites = ["Beyblades", "Naruto", "Stranger Things", "Dragon Ball Z", "The Office", "Modern Family"]
# favorites[1] = "Boruto"
# print(favorites[0])
#
# print(favorites)
#
# for i in favorites:
#     print(i)

# favorites = ["Beyblades", "Naruto", "Stranger Things", "Dragon Ball Z", "The Office", "Modern Family"]
# favorites.append("How I Met Your Mother")   # insert an item to the last index of a list
# print(favorites)

# favorites = ["Beyblades", "Naruto", "Stranger Things", "Dragon Ball Z", "The Office", "Modern Family"]
# favorites.remove("Beyblades")  # removes the character which is similar to the argument passed to the "remove" method
# print(favorites)

# favorites = ["Beyblades", "Naruto", "Stranger Things", "Dragon Ball Z", "The Office", "Modern Family"]
# favorites.pop(0)   # can delete the certain item in a list by passing the specific index as a argument to the "pop" method
# print(favorites)

# favorites = ["Beyblades", "Naruto", "Stranger Things", "Dragon Ball Z", "The Office", "Modern Family"]
# favorites.insert(3, "Teen Titans GO!")  # can insert an item to the list by first passing the index we want to be added and at second the item itself as the parameter
# print(favorites)

# favorites = ["Beyblades", "Naruto", "Stranger Things", "Dragon Ball Z", "The Office", "Modern Family"]
# favorites.sort()  # sorts to the alphabetical order
# print(favorites)

# numbers = [1301166, 1966, 66, 1776, 1999]
# numbers.sort()  # by default sorts values in ascending order
# print(numbers)

# numbers = [1301166, 1966, 66, 1776, 1999]
# numbers.sort(reverse=True)  # reverse parameter's value to True will make the sort in descending order
# print(numbers)

# favorites = ["Beyblades", "Naruto", "Stranger Things", "Dragon Ball Z", "The Office", "Modern Family"]
# favorites.clear()   # every item will be deleted creating an empty list
# print(favorites)



# list append and extend
# marks = [72,65,45,83,87]
# marks1 = [56,65,89]

# count = 0
# while count < 5:
    # print(marks[count])
    # count +=1
# marks.append(78)
# print(marks)
# marks.extend([90,89])
# print(marks)
# print(set(marks))

# 2D Lists
# sports = ["cricket", "football", "rugby", "basketball"]
# food = ["pizza", "spaghetti", "sandwiches", "burgers", "fries"]
# animes = ["Naruto", "Dragon Ball Z", "Deltora Quest", "Death Note", "Attack on Titan"]
# twod_list = [sports, food, animes]   # a 2D List
# print(twod_list)
# print(twod_list[2])
# print(twod_list[2][0])



# tuples
# student = ("supun", 22, "male")
# print(student.count("supun"))  # counts how many times a certain value appears in the tuple
# print(student.index(22))  # outputs the certain index
# print()
# for i in student:  # can use a for loop to print the values in a tuple
#     print(i)
# print()
# if "supun" in student:  # can use if statement to check the availability of a certain item
#     print("supun is here in the tuple!")



# sets
# utensils = {"fork", "spoon", "knife", "spoon", "spoon", "spoon"}  # does not print any duplicates since its un-indexed order changes
# dishes = {"plate", "bowl", "cup", "cup", "fork"}
# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# utensils.update(dishes)
# for i in utensils:
#     print(i)

# dinner_table = utensils.union(dishes)  # typical \/ of sets
# for i in dinner_table:
#     print(i)

# print(utensils.difference(dishes))
# print(utensils.intersection(dishes))   # typical /\ of sets



# dictionaries
# capitals = {"The USA": "Washington DC",
#             "Japan": "Tokyo",
#             "Australia": "Sydney",
#             "The UK": "London",
#             "France": "Paris"}
# print(capitals["The USA"])
# print(capitals.get("The USA"))   # this is much safer since if the key is not available it'll output "None"
# print(capitals.keys())    # outputs only the keys
# print(capitals.values())  # outputs only the values
# print(capitals.items())   # outputs all the items

# for country, capital_city in capitals.items():
#     print(country, ": ", capital_city)


# capitals.update({"Germany": "Berlin"})
# capitals.pop("The USA")
# capitals.clear()
# for country, capital_city in capitals.items():
#     print(country, ": ", capital_city)


