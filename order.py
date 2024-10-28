import menu1

def take_order():    #this function is define to take order from user
    print("Menu:")
    menu = menu1.getmenu()
    
    for key, value in menu.items():
        print(f"{key}: {value['item']} - ${value['price']}")
    order = {}
    while True:
        choice = input("Enter the item number to order (press 'done' to finish): ")     #user choice to order the food
        
        if choice.lower() == 'done':  #if user does not want any more food so he/she can click done
            break
        
        if choice in menu:
            quantity = int(input(f"Enter quantity for {menu[choice]['item']}: "))
            order[menu[choice]['item']] = quantity
        
        else:
            print("Invalid choice! Please choose a valid item number.")     #if user input invalid food number
    
    return order

def calculate_total(order):             #this function will calculate amount and billof user
    menu = menu1.getmenu()
    total = 0
    for item, quantity in order.items():
        for key, value in menu.items():
            if value['item'] == item:
                total += value['price'] * quantity             #it will calculate their total amount of their order
    return total





## Restaurant Order Management System

#This is a simple Python program for managing restaurant orders. Users can view the menu, place orders, and calculate the total amount.
#
## Features
#
# View menu items with prices.
# Place orders by selecting item numbers.
# Calculate the total amount for the order