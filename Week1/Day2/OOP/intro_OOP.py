#1.
# OOP:

# Object Oriented Programming
    # Style of programming uses a blueprint for modeling data
    # Blueprint defined by the programmer -- DIY datatypes
    #    -- customize it for your situation
    # Modularizing

# 2:
# What is CLASS:
    # User/Programmer defined data-type
    # Like a function is a recipe --- class is blueprint for the datatype

# 3. What are...

# Attributes/properties
    # Characteristics -- variables that belong to the class
    # What a class of objects HAS --> data
        #ex: car
            # -- model -- string (corolla)
            # -- make -- string (toyota)
    # JS: my_arr = [3, 4, 5]
    # console.log( my_arr.length )

# Methods
    # Functions that often affect the properties of the class
    # Functions that belong to the class -- 
    # What a class of objects can DO --> actions/functions

my_list = [3, 4, 5]
my_list.append(8) # --> [3, 4, 5, 8]

# Quiz Challenge:

# self.store = store
# self.items.append(item)   
# def add_item(self, item, price):   
# self.items = []
# def __init__(self, store):
# class ShoppingCart:
# return self
# self.total = 0
# self.total += price


class ShoppingCart:

    def __init__(self, specific_store):
        self.total = 0
        self.store = specific_store
        self.items = []

    def add_item(self, thing, price):
        self.total += price
        self.items.append(thing)
        return self

    def show_cart(self):
        print(f"Store: {self.store}, total: {self.total}")
        print(f"Items: {self.items}")

sadie_shopping_cart = ShoppingCart("Safeway")
print(sadie_shopping_cart)
print(sadie_shopping_cart.store)

nate_cart = ShoppingCart("Target")
print(nate_cart)
print(nate_cart.store)

nate_cart.store = "Amazon"
nate_cart.items.append("apples")
nate_cart.total += 3.00

nate_cart.add_item("apples", 3.00)
nate_cart.add_item("pears", 3.00)
nate_cart.add_item("broccoli", 5.00)

# nate_cart.items.append("mango")
# nate_cart.total += 5.0

# nate_cart.show_cart()

# sadie_shopping_cart.show_cart()


# nate_cart.add_item("Star Wars Figurine", 50.00)
# nate_cart.add_item("apple", 0.99)
