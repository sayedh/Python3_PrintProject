# GRAND OPENING of our new Burgers on the Grill Restaurant


# importing defined funcions from file and modules
from functions import draw_shape
import functions
from functions import orders
from functions import sales
from os.path import join
from functions import place_record, rotate_record, drop_needle
from datetime import datetime





# Example of a basic print statement
# Restaurant name
print("Burgers on the Grill")





# Join strings using the join feature
weekdays = "Tue, Wed, Thurs, Fri "
weekends = " Sat, Sun"
opening_hour= "10am"
closing_hour = "8pm"
print("We are OPEN: ", join(weekdays, weekends))


# Create my own join function
def myjoin(*args):
    joined_string = args[0]
    for arg in args[1:]:
        joined_string += '-' + arg
    return joined_string
print("Our hours are: ", myjoin(opening_hour, closing_hour), "\n")





# Call a function from another file  - "functions.py"
def play_record(album):
    place_record(album)
    rotate_record(album)
    drop_needle(album)

next_album = "Bubble Gum / Mr. Loco"
play_record(next_album)





# Use None as a placeholder in an if statement
session_id = None
if session_id is None:
    print("\nWELCOME! Please take a look at our menu!\n")




# Example of .append in Python
def update_order(new_item, current_order=None):
    if current_order is None:
        current_order = []
    current_order.append(new_item)
    return current_order
order1 = update_order({'item': 'burger', 'cost': '3.50'})
order1 = update_order({'item': 'soda', 'cost': '1.50'}, order1)
order2 = update_order({'item': 'soda', 'cost': '1.50'})
print("Order#1", order1)
print("Order#2", order2, "\n")




# Extract the cost for the items from order1
values = [val['cost'] for val in order1]
values_floats = []
for item in values:
    values_floats.append(float(item))

# Creating a SUM calculator
def SUM(num1, num2):
    sum = num1 + num2
    return sum

sum = SUM(values_floats[0], values_floats[1])
print("Order#1 Total: $", sum)

# Extract the cost for the items from order2
values = [val['cost'] for val in order2]
values_floats = []
for item in values:
    values_floats.append(float(item))

# Creating a SUM calculator
def SUM(num1):
    sum = num1
    return sum

sum = SUM(values_floats[0])
print("Order#2 Total: $", sum, "\n")





#  Control the case of the letters
def loudly(text):
    loudly = text.upper()
    return loudly

def politely(text):
    politely = text.lower()
    return politely

loud = loudly("We are preparing your order!")
polite = politely("Please take a seat.")
print(loud, polite, '\n')





# Set an arbitrary number of arguments. 
def shout_strings(*args):
    for argument in args:
        print(argument.upper())
shout_strings("Get ready to taste our delicious burgers! (っ ͡⚈ ͜ʖ ͡⚈)っ",
 "AND here is a warm drink on the house",
"""
 ▄▀ ▄▀
  ▀  ▀
█▀▀▀▀▀█▄
█░░░░░█─█
▀▄▄▄▄▄▀▀
\n""")






# Cut off your string after a specified length. 
def cut_string(length, *sentences):
    for sentence in sentences:
        print(sentence[:length])

cut_string(26, "Hope you enjoyed the food." , "( ͡▀̿ ̿ ‿っ ͡▀̿ ̿ )✌ \n                  ")





# Define any number of arguments and call it
def arbitrary_args(**kwargs):
    print(kwargs.get('line_break'))

arbitrary_args(secret_recipe="XXXXXXXX", ketchup="mayo", cheese="cheddar", line_break="     ")





# Use {}.format to input more strings into strings
print("The {name} is a {adjective} place to go. I'm going to rate it {feeling}.\n\n".format(name="Burgers on the Grill", adjective="great", feeling="10/10",))





# Build a function to print the total counts
print("Managerial Accounting:")
def accounting(**products_dict):
    for name, count in products_dict.items():
        orders(name, count)
accounting(Burger='79', Drink='114')
print("\n", end="")





# Use a dictionary item list for the arguments
def accounting(**products_dict):
    for name, price in products_dict.items():
        sales(name, price)

sales_dict = {'Burger': 276.5, 'Drinks': 171}
accounting(**sales_dict)
print("\n", end="")


# Select the values from the dictionary list and add them and print the total
total = sales_dict.get('Burger') + sales_dict.get('Drinks')
def total_sales(total):
    print("Today we made ${}!\n".format(total))
returned_value = total_sales(float(total))
print("\n")




# Use a Python decorator to tell time
def info(func):
    def inner():
        print("What time is it?")
        func()
    return inner()
@info
def time():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print("It is ", current_time, "\nPSH! No, it's burger time!")






# Call function from file and Print the the Burger Logo
def draw_shape(shape_name, character, line_breaks):
    shape = functions.draw_shape(shape_name, character)
    if not line_breaks:
        print(shape[1:-1])
    else:
        print(shape)
draw_shape(shape_name="burger", character='o', line_breaks=True)