'''
Book delivery
specials
customers
'''

from cust_functions import *
from employee_functions import *
import time
#import coffee_dicts

print("Welcome to Frankie's Bookshop")
time.sleep(1)
# main menu
while True:
    prompt = "What would you like to do?:\n"
    prompt += "-[P]roducts to order\n-[A]dditional Options\n-[E]mployee Options\n-[R]eviw Order\n-[F]inish order\n-[Q]uit\n>"
    
    choice = input(prompt)
    # call appropriate functions
    if choice.lower() == "p":
        order_product_menu()
    elif choice.lower() == "f":
        finish_order()
        time.sleep(1)
        print("Returning to main menu...\n\n")
    elif choice.lower() == "a":
        cust_options()
    elif choice.lower() == "r":
        review_order()
    elif choice.lower() == "e":
        emp_functions()
    elif choice.lower() == "q":
        print("Closing app...")
        time.sleep(1)
        break
    else:
        print("Please make a valid selection!")
        continue

#NOT DONE
#-Check price doesn't refresh items
#-Orders don't subtract from stock
