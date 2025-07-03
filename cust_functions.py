import time
import coffee_dicts
from employee_functions import *

# three order dictionaries for each category of product
book_order = []
coffee_order = []
food_order = []
# "promotion" used to apply discount by multiplying total by promotion, e.g. 1 = no promotion, 0.75 = 25% discount, 0.5 = 50% discount, etc. Update through employee function.
promotion = 1
# "percentage" used to represent discount as a string.
percentage = 100
# personal_coffee_price declared so that custom coffees can be calculated separately then added to order.
personal_coffee_price = 0

'''The following functions are related to customer functionality'''

def cust_options():
    # Display additional customer options
    prompt = "Please choose from the following options:\n"
    prompt += "-Describe [P]roduct\n-[B]ook Delivery\n-[R]eturn\n>"
    cust_opt_choice = input(prompt)
    if cust_opt_choice.lower() == "r":
        print("\nReturning...")
        time.sleep(1)
    elif cust_opt_choice.lower() == "p":
        describe_product()
    elif cust_opt_choice.lower() == "b":
        book_delivery()
        time.sleep(1)
    else:
        print("\nPlease make a valid selection!\n")
        time.sleep(1)

def book_delivery():
    delivery_details = {}
    print("please enter the following details to order a book:")
    for x in coffee_dicts.books.keys():
        print("-" + x)
    # Gather book details
    name = input("Enter your name:\n>")
    house_number = input("Enter your house number\n>")
    street = input("Enter the street name\n>")
    town = input("Enter the town name\n>")
    postcode = input("Enter the postcode\n>")
    # Add the book to the dictionary
    delivery_details[name.title()] = {
        "Name": name.title(),
        "House Number": house_number,
        "Street Name": street,
        "Town": town,
        "Postcode" : postcode 
    }
    print(f"Your book has been ordered for delivery...\n")
    print(f"it will be delivered to:\n")
    for x, dict in delivery_details.items():
        for key,value in dict.items():
            print(value)
    time.sleep(3)

### select book for delivery

def describe_product():
    # List all products
    print("Available books:")
    for book in coffee_dicts.books.keys():
        print("-" + book)
    print("Available coffees:")
    for item in coffee_dicts.coffee.keys():
        print("-" + item)
    print("Available food:")
    for item in coffee_dicts.food_items.keys():
        print("-" + item)
    time.sleep(3)
    get_detail = input("\nWhich product do you want to know more about?\n>")
    # Verify selection exists in one of the product dictionaries, and if so return keys (x) and values (y)
    if get_detail.title() in coffee_dicts.books.keys():
        dict = coffee_dicts.books[get_detail.title()]
        print(f"The details for {get_detail.title()} are:")
        for x, y in dict.items():
            print(x + ':' + str(y))
        time.sleep(3)
    elif get_detail.title() in coffee_dicts.coffee.keys():
        dict = coffee_dicts.coffee[get_detail.title()]
        print(f"The details for {get_detail.title()} are:")
        for x, y in dict.items():
            print(x + ':' + str(y))
        time.sleep(3)
    elif get_detail.title() in coffee_dicts.food_items.keys():
        dict = coffee_dicts.food_items[get_detail.title()]
        print(f"The details for {get_detail.title()} are:")
        for x, y in dict.items():
            print(x + ':' + str(y))
        time.sleep(3)
    else:
        print("\nPlease make a valid selection!\n")
        time.sleep(1)

def order_product_menu():
    prompt = "Please choose from the following options:\n"
    prompt += "-[B]ooks\n-[C]offees\n-[F]ood\n-[R]eturn\n>"
    prod_menu_choice = input(prompt)
    if prod_menu_choice.lower() == "r":
        print("\nReturning...")
        time.sleep(1)
    elif prod_menu_choice.lower() == "b":
        order_book()
    elif prod_menu_choice.lower() == "c":
        order_coffee()
    elif prod_menu_choice.lower() == 'f':
        order_food()
        time.sleep(1)
    else:
        print("Please make a valid selection")
        time.sleep(1)

def order_food():
    # List available foods
    print("The following snacks are available:")
    for x in coffee_dicts.food_items.keys():
        print(f"-{x}")
    # Capture user choice
    food_choice = input("\nWhat would you like to order?\n>")
    # verify choice in dictionary
    if food_choice.title() not in coffee_dicts.food_items.keys():
        print("Please make a valid selection!\n")
        time.sleep(1)
    # add selection to order
    else:
        food_order.append(food_choice.title())
        print(f"\nYou have ordered {food_choice.title()}\n")
        time.sleep(1)
    # reduce stock level by one
    for item in food_order:
        coffee_dicts.food_items[item]["Stock"] -= 1

def order_book ():
    # display products, and append choice to relevant order list
    print(f"\nWe have the following books available:\n")
    for title in coffee_dicts.books.keys():
        print(f"-{title}")
    book_choice = input("\nWhich book would you like?\n>")
    if book_choice.title() not in coffee_dicts.books.keys():
        print("Please make a valid selection!\n")
        time.sleep(1)
    else:
        book_order.append(book_choice.title())
        print(f"\nYou have ordered {book_choice.title()}\n")
        time.sleep(1)
    for item in book_order:
        coffee_dicts.books[item]["Stock"] -= 1
    
def order_coffee():
    # display products, and append choice to relevant order list
    print(f"\nWe have the following coffees available:\n")
    for drink in coffee_dicts.coffee.keys():
        print(f"-{drink}")
    coffee_choice = input("\nWhich coffee would you like?\n>")
    if coffee_choice.lower() == 'custom coffee':
        custom_coffee()
    elif coffee_choice.title() not in coffee_dicts.coffee.keys():
        print("\nPlease make a valid selection!\n")
        time.sleep(1)
    else:
        coffee_order.append(coffee_choice.title())
        print(f"\nYou have ordered {coffee_choice.title()}\n")
        time.sleep(1)

def custom_coffee():
    # global variables can be read within a function, but if you want to change them you need to make them accessible with "global [VARIABLE]"
    global coffee_order
    global personal_coffee_price
    personal_coffee = []
    print(f"\nPlease select from the following options for your custom coffee:\n")
    time.sleep(1)
    # show custom options and prices - formatted correctly
    print("Item\t\tPrice")
    for x,y in coffee_dicts.custom_coffee_prices.items():
        print(f"-{x}\t{y}")
    time.sleep(1)
    while True:
        # use a while loop because we don't know how many items the customer wants to add
        prompt = "What would you like in your coffee? ([D]one)\n>"
        custom_order = input(prompt)
        if custom_order.lower() == 'd':
            # summarise order and calculate price
            print("Your order is...")
            for x in personal_coffee:
                print(f"-{x}")
            print(f"Your coffee will cost:\t{sum(coffee_dicts.custom_coffee_prices[item] for item in personal_coffee)}")
            time.sleep(1)
            break
        elif custom_order.lower() == 'foam':
            # for formatting purposes foam doesn't align without a '\n', which isn't matched by customer input, therefore it needs to be handled separately.
            print("Adding foam to your order...")
            time.sleep(1)
            # append "foam\t" to order list rather than "foam" to facilitate match
            personal_coffee.append("foam\t")
        elif custom_order.lower() in coffee_dicts.custom_coffee_prices.keys():
            print(f"Adding {custom_order.lower()} to your order...")
            time.sleep(1)
            personal_coffee.append(custom_order)
            time.sleep(1)
        else:
            print("\nPlease make a valid selection!\n")
            time.sleep(1)
    # add "custom coffee" to order, then calculate and store price for adding to total later.
    coffee_order.append("Custom Coffee")
    personal_coffee_price = sum(coffee_dicts.custom_coffee_prices[item] for item in personal_coffee)

def review_order():
    print("\nYour current order is: ")
    print("Books:")
    for item in book_order:
        print(f"-{item}")
    print("Coffees:")
    for item in coffee_order:
        print(f"-{item}")
    print("Food:")
    for item in food_order:
        print(f"-{item}")
    print("\n")
    time.sleep(3)

def finish_order():
    print("Your final total is:\n")
    print("Books:")
    for item in book_order:
        print(f"-{item}")
    print("Coffees:")
    for item in coffee_order:
        print(f"-{item}")
    print("\n...\n")
    total_books_cost = sum(coffee_dicts.books[item]["Price"] for item in book_order)
    total_coffees_cost = sum(coffee_dicts.coffee[item]["Price"] for item in coffee_order)
    total_food_cost = sum(coffee_dicts.food_items[item]["Price"] for item in food_order)
    if promotion < 1:
        total_cost = (total_books_cost + total_coffees_cost + total_food_cost + personal_coffee_price) * promotion
        print(f"You have received a discount of {str(percentage)}%")
        print(f"The total cost of your order is: £{total_cost:.2f}\n")
    else:
        total_cost = (total_books_cost + total_coffees_cost + total_food_cost + personal_coffee_price)
        print(f"The total cost of your order is: £{total_cost:.2f}\n")