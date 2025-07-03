import time
import coffee_dicts
import cust_functions

'''This section contains all functions relevant to employees'''

def emp_functions():
    # Limit login attempts to 3
    login_tries = 1
    while login_tries < 4:
        # Check username against employees dictionary
        emp_user = str(input("Please enter your username:\n>"))
        if emp_user in coffee_dicts.employees.keys():
            # if username is present, check password against dictionary
            emp_password = str(input("Please enter your password:\n>"))
            if emp_password == coffee_dicts.employees[emp_user]:
                # Displayy options and capture input
                prompt = "Please choose from the following options:\n"
                prompt += "-[U]pdate Stock\n-[A]dd New Item\n-Apply [P]romotion\n-[B]ack\n>"
                emp_opt_choice = input(prompt)
                # Call different functions or return based on input
                if emp_opt_choice.lower() == "u":
                    update_stock()
                    break
                if emp_opt_choice.lower() == "a":
                    new_item()
                    break
                if emp_opt_choice.lower() == "p":
                    apply_promotion()
                    break
                if emp_opt_choice.lower() == "b":
                    print("Returning to main menu...")
                    time.sleep(1)
                    break
            else:
                # Increment login attempts if password is incorrect
                print("Please enter a valid password...")
                login_tries += 1
                time.sleep(1)
        elif emp_user not in coffee_dicts.employees.keys():
            print("Please enter a valid username")
            time.sleep(1)

def new_item():
    # adding different product types requires different processes, so call appropriate function
    add_type = input("Add a new:\n-[b]ook\n-[c]offee\n-[f]ood\n-[R]eturn\n>")
    if add_type.lower() == "b":
        new_book()
    if add_type.lower() == "c":
        new_coffee()
    if add_type.lower() == "f":
        new_food()
    if add_type.lower() == "r":
        print("Returning to main menu...")
        time.sleep(1)

def new_book():
    print("Available books:")
    for x in coffee_dicts.books.keys():
        print("-" + x)
    # Gather book details
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    genre = input("Enter the genre: ")
    price = float(input("Enter the book price: "))
    stock = int(input("Enter the stock quantity: "))
    # Add the book to the dictionary
    coffee_dicts.books[title.title()] = {
        "Author": author.title(),
        "Genre": genre.title(),
        "Price": price,
        "Stock": stock
    }
    print(f"Book '{title}' has been added successfully!\n")
    print("Available books:")
    for x in coffee_dicts.books.keys():
        print("-" + x)
    time.sleep(1)

def new_coffee():
    print("Available coffees:")
    for x in coffee_dicts.coffee.keys():
        print("-" + x)
    time.sleep(1)
    # Gather coffee details
    title = input("Enter the name of the new coffee: ")
    description = input("Enter the description of the: ")
    price = float(input("Enter the price: "))
    stock = int(input("Enter the quantity in stock: "))
    # Add the coffee to the dictionary
    coffee_dicts.coffee[title.title()] = {
        "Description": description,
        "Price": price,
        "Stock": stock
    }
    print(f"Coffee '{title.title()}' has been added successfully!\n")
    print("Available coffees:")
    for x in coffee_dicts.coffee.keys():
        print("-" + x)
    time.sleep(1)

def new_food():
    print("Coming soon...")
    time.sleep(1)
    for x in coffee_dicts.food_items.keys():
        print("-" + x)
    # Gather food details
    name = input("Enter the name of the new food item:\n>")
    type = input("Enter the type of food item:\n>")
    description = input("Enter a description of the product:\n>")
    # ingredients is a list in the dictionary, capture each item and add to an empty list
    ingredients_list = []
    while True:
        ingredient = input("Enter the ingredients in the product or [d]one:\n>")
        if ingredient == "d":
            for x in ingredients_list:
                print(f"Adding {x}")
            break
        else:
            ingredients_list.append(ingredient)
    price = float(input("Enter the product price:\n>"))
    stock = int(input("Enter the stock quantity:\n>"))
    # Create a dictionary for new item, and add to existing foods dic'
    coffee_dicts.food_items[name.title()] = {
        "Type": type.title(),
        "Description": description.title(),
        "Ingredients" : [],
        "Price": price,
        "Stock": stock
    }
    # add items from ingredients_list into ingredients in dictionary
    for x in ingredients_list:        
        coffee_dicts.food_items[name.title()]["Ingredients"].append(x)
    print(f"Food item: '{name}' has been added successfully!\n")
    time.sleep(1)
    print("Available foods:")
    for x in coffee_dicts.food_items.keys():
        print("-" + x)
    time.sleep(1)

def update_stock():
    # update stock menu
    while True:
        update_stock = input("Update stock levels for:\n-[b]ooks\n-[c]offee\n-[f]ood\n-[R]eturn\n>")
        if update_stock.lower() == 'c':
            coffee_stock()
        elif update_stock.lower() == 'b':
            book_stock()
        elif update_stock.lower() == 'f':
            food_stock()
        elif update_stock.lower() == 'r':
            print("Returning to main menu...")
            time.sleep(1)
            break
        else:
            print("Please make a valid selection!\n")
            time.sleep(1)

def food_stock():
    # try/except to capture invalid inputs and avoid crash
    try:
        # display items and capture selection
        for title in coffee_dicts.food_items.keys():
            print(title)
        select_food = input("Which product do you want to add stock for?\n>")
        check_stock = int(coffee_dicts.food_items[select_food.title()]["Stock"])
        print(f"You currently have {check_stock} servings of {select_food} stock\n")
        try:
            new_stock = int(input("\nHow many would you like to add\n>"))
            print(f"\nAdding {new_stock} to inventory...")
            # make a new dictionary KVP, then update existing dictionary value
            update_inv = {"Stock" : (check_stock + new_stock)}
            coffee_dicts.food_items[select_food.title()].update(update_inv)
            # confirm updated stock levels
            print("\nThere are now " + str(coffee_dicts.food_items[select_food.title()]["Stock"]) + " servings of " + select_food.title() + " in stock.\n")
            time.sleep(1)
        # catch incorrect stock values (non-integer)
        except ValueError:
            print("Please enter a valid value")
            time.sleep(1)
    # catch incorrect item names - fails if not exists
    except KeyError:
        print("Please enter a valid value")
        time.sleep(1)

def book_stock():
    try:
        for title in coffee_dicts.books.keys():
            print(title)
        select_book = input("Which book do you want to add stock for?\n>")
        check_stock = int(coffee_dicts.books[select_book.title()]["Stock"])
        print(f"You currently have {check_stock} copies in stock\n")
        try:
            new_stock = int(input("\nHow many would you like to add\n>"))
            print(f"\nAdding {new_stock} to inventory...")
            update_inv = {"Stock" : (check_stock + new_stock)}
            coffee_dicts.books[select_book.title()].update(update_inv)
            print("\nThere are now " + str(coffee_dicts.books[select_book.title()]["Stock"]) + " copies of " + select_book.title() + " in stock.\n")
        except ValueError:
            print("Please enter a valid value")
            time.sleep(1)
    except KeyError:
        print("Please enter a valid value")
        time.sleep(1)

def coffee_stock():
    try:
        for title in coffee_dicts.coffee.keys():
            print(title)
        select_coffee = input("\nWhich coffee do you want to add stock for?\n>")
        check_stock = int(coffee_dicts.coffee[select_coffee.title()]["Stock"])
        print(f"\nYou currently have enough supplies to make {check_stock} coffees\n")
        try:
            new_stock = int(input("\nHow many would you like to add\n>"))
            print(f"\nAdding {new_stock} to inventory...\n")
            update_inv = {"Stock" : (check_stock + new_stock)}
            coffee_dicts.coffee[select_coffee.title()].update(update_inv)
            print("\nYou now have enough to make " + str(coffee_dicts.coffee[select_coffee.title()]["Stock"]) + " " + select_coffee.title() + "s in stock.\n")
        except ValueError:
            print("Please enter a valid value")
            time.sleep(1)
    except KeyError:
        print("Please enter a valid value")
        time.sleep(1)

def apply_promotion():
    global promotion
    global percentage
    discount = (input("Please type the percentage discount to be applied, or [R]emove currently active discount\n>"))
    if discount.lower() == 'r':
        promotion = 1
        print("Promotional discount has been removed")
    elif int(discount) in range(101):
        percentage = int(discount)
        cust_functions.promotion = cust_functions.promotion - (int(discount) / 100)
        print(f"\nA discount of {discount}% will be applied to orders\n")
    else:
        print("Please make a valid selection")