# Python

# [X] Virtual Environment
# [X] Version -- 3.6

# [X] Printing
# [X] f-strings

greeting = "Guten tag"
name = "Allen"
age = 25

# Guten tag, Allen! You are 25 years old.
print(f"{greeting}, {name}! You are {age} years old")

# [ ] Variables

# [X] Data Types

    # [X] Primitive types --- value types
        # boolean
        # float / double / long --> decimals
        # string
        # integers

sadie_age = 38
michael_age = 22

# makes a copy of michael_age (22) and stores it in sadie_age
sadie_age = michael_age
michael_age = michael_age + 4


# [X] Composite (data types that hold multiple values)
    #     --- reference types
    #             0  1  2  3  4
    # lists ---> [3, 4, 5, 6, 7]
    # dictionaries --> key, value pairs
    # tuple  (2, 2, 4, 5)

sadieList = [3, 4, 5, 6]
michaelList = [2, 2, 2, 2]

# Shallow copy (2 variables pointing to the same thing)
sadieList = michaelList

# Deep copy 
# 2 different lists in memory that have the same values, 
# but are separate
sadieList = []
for idx in range(len(michaelList)):
    sadieList.append(michaelList[idx])

michaelList[2] += 4

user = {
    "first_name": "Sadie", 
    "last_name": "Flick"
}

print(user)

# [X] whitespace
#   ---> scope within if statements, for loops, 
#        or other scopes, and later class definitions
#        require indentation - 
#   ---> must be either all same amount of spaces, 
#        or tabs. Cannot mix spaces and tabs.
#   ---> Note VS code inserts 4 spaces when you press tab.

def weatherPrep(currentWeather):

    if (currentWeather == "Cloudy"):
        print("Bring a jacket.")

    elif (currentWeather == "Rainy"):
        print("bring an umbrella")

    else:
        print("Wear whatever")


# weatherPrep("Rainy")

# [X] Conditionals
# [ ] Loops
# [X] Functions
    #   Review