"""
Name: Michael Hunter
Student Number: C19365646
Date of submission: 17th of December 2020
Compiler: PyCharm Education Edition
Operating System: Windows 10

Program Description: This program is designed for the purpose of a virtual store, where the user can basically buy any item that is available in the world. Its based around the current situation in the world where stores operate through a click and collect or delivery.
                     The user first enters their details along with the date and the everyday question of if they have covid symptoms before even starting their shop. Here at Active Hunter we have weekly items for both the bargain hunters out there and we sell exclusive
                     items to those with our loyalty cards. Loyalty card holders also can receive 10 % off at the checkout. We at Active Hunter also accept multiple currencies due to our stores being across Europe, America and Australia.

Additionals files: items_available and items_available2
"""
# Declaring the class ItemToPurchase so that the user can manually add their items
class ItemToPurchase:
    # Parameter construction for the class ItemToPurchase
    def __init__(self, item_name='none', item_price=0.0, item_quantity=0, item_description='none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    # Implement the method
    def print_item_cost(self):
        # print the output in a specified format
        string = '{} {} @ €{} = €{}'.format(self.item_name, self.item_quantity, self.item_price, (self.item_quantity * self.item_price))
        cost = self.item_quantity * self.item_price
        return string, cost

    # Implement the method print_item_description
    def print_item_description(self):
        string = '{}: {}'.format(self.item_name, self.item_description)
        print(string, end='\n')
        return string

# Declare the class ShoppingCart
class ShoppingCart:
    # Parameter construction for the class ShoppingCart
    def __init__(self, customer_name='none', current_date='none', cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    # Implement method loyal_customer
    def loyalty_card(self):
        while True:
            card = int(input('Please enter your 10 digit loyalty card number:'))
            if card == 1234567890:
                print('Your loyalty card number has been entered correctly.')
                print('Please take a look at what items we currently have on special offer for our loyal customers this week.')
                # open and read the file after the appending:
                item_list = open("items_available.txt", "r")
                print(item_list.read())
                break
            else:
                print('Your loyalty card number has been entered incorrectly please try again!')
                print_menu(ShoppingCart)

    # Implement method bargain hunter
    def bargain_hunter(self):
        # open and read the file after the appending:
        item_list2 = open("items_available2.txt", "r")
        print(item_list2.read())

    # Implement method to add item in the shopping cart
    def add_item(self):
        print('\nADD ITEM TO CART', end='\n')
        # prompt the name and description of item,price and quantity
        item_name = str(input('Enter the item name: '))
        item_description = str(input('Enter the item description: '))
        item_price = float(input('Enter the item price: '))
        item_quantity = int(input('Enter the item quantity: '))
        # Append the above values in to the list
        self.cart_items.append(ItemToPurchase(item_name, item_price, item_quantity, item_description))

    # Implement the method to delete the item in the cart
    def remove_item(self):
        print('\nREMOVE ITEM FROM CART', end='\n')
        # prompt the item to remove the list
        string = str(input('Enter name of item to remove: '))
        i = 0
        # Using for-loop to iterate every item
        for item in self.cart_items:
            # If item found delete in the list
            if(item.item_name == string):
                del self.cart_items[i]
                i += 1
                # set the flag value to true
                # break from the list
                flag = True
                break
            # Otherwise set value to false
            else:
                flag = False
        # IF the value not found
        if(flag is False):
            # print the message
            print('Item not found in cart. Nothing removed')

    # Implement the method
    def modify_item(self):
        print('\nCHANGE ITEM QUANTITY', end='\n')
        # Prompt the input item
        name = str(input('Enter the item name: '))
        # Using for-loop to iterate every item
        for item in self.cart_items:
            # If item found update Quantity in the list
            if(item.item_name == name):
                quantity = int(input('Enter the new quantity: '))
                item.item_quantity = quantity
                # set the flag value to true
                # break from the list
                flag = True
                break
            # Otherwise set value to false
            else:
                flag = False
        # IF the value not found
        if(flag is False):
            # print the message
            print('Item not found in cart. Nothing modified')

    # implement method to compute total number of items in the cart
    def get_num_items_in_cart(self):
        num_items = 0
        # Using for-loop to iterate the cart
        for item in self.cart_items:
            # ADD the Quantities
            num_items = num_items+item.item_quantity
        # return the num_Items
        return num_items

    # Implement the method
    def get_cost_of_cart(self):
        total_cost = 0
        cost = 0
        # Using for-loop to iterate the list
        # multiply the price and Quantity
        # add value to the Total_Cost
        for item in self.cart_items:
            cost = (item.item_quantity * item.item_price)
            total_cost += cost
        # return the value
        return total_cost

    # Implement the method to print the total
    def print_total(self):
        total_cost = self.get_cost_of_cart()
        if (total_cost == 0):
            print('SHOPPING CART IS EMPTY')
        else:
            self.output_cart()

    # Implement the method to print_descriptions
    def print_descriptions(self):
        print('\nOUTPUT ITEMS\' DESCRIPTIONS')
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date), end='\n')
        print('\nItem Descriptions', end='\n')
        for item in self.cart_items:
            print('{}: {}'.format(item.item_name, item.item_description), end='\n')

    # Implement the method output_cart()
    def output_cart(self):
        new = ShoppingCart()
        print('\nOUTPUT SHOPPING CART', end='\n')
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date), end='\n')
        print('Number of Items:', new.get_num_items_in_cart(), end='\n\n')
        total_cost = 0
        currency_converter = ('\nMENU\n'
        'eu - Euro\n'                      
        'usd - American Dollars\n'                      
        'po - British Pounds\n'                      
        'aud - Australian Dollars\n'
        'ret - Return to the main menu\n')
        payment = ''
        # Using while loop
        # to iterate until the user enters ret
        while(payment != 'ret'):
            print(currency_converter, end='\n')
            # Prompt the Command
            payment = input('Select which the currency that you would wish to pay with: ')
            # repeat the loop until user enters the eu,usd,po,aud,other or ret command
            while(payment != 'eu' and payment != 'usd' and payment != 'po' and payment != 'aud' and payment != 'ret'):
                payment = input('Select which the currency that you would wish to pay with: ')
            # If the input payment is eu
            if(payment == 'eu'):
                for item in self.cart_items:
                    print('{} {} @ €{} = €{}'.format(item.item_name, item.item_quantity, item.item_price, (item.item_quantity * item.item_price)), end='\n')
                    total_cost += (item.item_quantity * item.item_price)
                    # This allows loyalty users to also get a 10% discount at the checkout when using their loyalty card
                    card = int(input('Please enter your 10 digit loyalty card number:'))
                    if card == 1234567890:
                        total_cost = (total_cost * 0.90)
                    else:
                        total_cost = (total_cost / 1.90 * 1)
                print('\nTotal: €{}'.format(total_cost), end='\n')
            # If the input payment is usd
            if(payment == 'usd'):
                for item in self.cart_items:
                    print('{} {} @ €{} * $1.23 = ${}'.format(item.item_name, item.item_quantity, item.item_price, ((item.item_quantity * item.item_price) * 1.23)), end='\n')
                    total_cost += ((item.item_quantity * item.item_price) * 1.23)
                    # This allows loyalty users to also get a 10% discount at the checkout when using their loyalty card
                    card = int(input('Please enter your 10 digit loyalty card number:'))
                    if card == 1234567890:
                        total_cost = (total_cost * 0.90)
                    else:
                        total_cost = (total_cost / 1.90 * 1)
                print('\nTotal: ${}'.format(total_cost), end='\n')
            # If the input payment is po
            if(payment == 'po'):
                for item in self.cart_items:
                    print('{} {} @ €{} * £0.90 = £{}'.format(item.item_name, item.item_quantity, item.item_price, ((item.item_quantity * item.item_price) * 0.90)), end='\n')
                    total_cost += ((item.item_quantity * item.item_price) * 0.9)
                    # This allows loyalty users to also get a 10% discount at the checkout when using their loyalty card
                    card = int(input('Please enter your 10 digit loyalty card number:'))
                    if card == 1234567890:
                        total_cost = (total_cost * 0.90)
                    else:
                        total_cost = (total_cost / 1.90 * 1)
                print('\nTotal: £{}'.format(total_cost), end='\n')
            # If the input payment is aud
            if(payment == 'aud'):
                for item in self.cart_items:
                    print('{} {} @ €{} * $1.61 = ${}'.format(item.item_name, item.item_quantity, item.item_price, ((item.item_quantity * item.item_price) * 1.61)), end='\n')
                    total_cost += ((item.item_quantity * item.item_price) * 1.61)
                    # This allows loyalty users to also get a 10% discount at the checkout when using their loyalty card
                    card = int(input('Please enter your 10 digit loyalty card number:'))
                    if card == 1234567890:
                        total_cost = (total_cost * 0.90)
                    else:
                        total_cost = (total_cost / 1.90 * 1)
                print('\nTotal: ${}'.format(total_cost), end='\n')
            # If the input payment is other
            if(payment == 'ret'):
                print('Returning to main menu we apologize for any lag that may occur during this transition.')

# Implement the method print_menu
def print_menu(ShoppingCart):
    customer_Cart = newCart
    # declare the string menu
    menu = ('\nMENU\n'
    'l - Loyal customer items\n'
    'b - Bargain hunter items\n'
    'a - Add item to cart\n'
    'r - Remove item from cart\n'
    'c - Change item quantity\n'
    'i - Output items\' descriptions\n'
    'o - Output shopping cart\n'
    'q - Quit\n')
    command = ''
    # Using while loop
    # to iterate until user enters q
    while(command != 'q'):
        string = ''
        print(menu, end='\n')
        # Prompt the Command
        command = input('Choose an option: ')
        # repeat the loop until user enters the l,b,a,o,i,r,c or q command
        while(command != 'l' and command != 'b' and command != 'a' and command != 'o' and command != 'i' and command != 'r'
              and command != 'c' and command != 'q'):
            command = input('Choose an option: ')
        # If the input command is l
        if(command == 'l'):
            # call the method to allow loyal customers to read what special items they can get a discount on this week
            customer_Cart.loyalty_card()
        # If the input command is b
        if(command == 'b'):
            # call the method to allow bargain hunters to read what items we have on sale this week
            customer_Cart.bargain_hunter()
        # If the input command is a
        if(command == 'a'):
            # call the method to the add elements to the cart
            customer_Cart.add_item()
        # If the input command is o
        if(command == 'o'):
            # call the method to the display the elements in the cart
            customer_Cart.output_cart()
        # If the input command is i
        if(command == 'i'):
            # call the method to the display the elements in the cart
            customer_Cart.print_descriptions()
        # If the input command is i
        if(command == 'r'):
            customer_Cart.remove_item()
        if(command == 'c'):
            customer_Cart.modify_item()
        if(command == 'q'):
            print('Thank you for shopping with us today. We hope you have a Merry Christmas and a Happy New Year. Stay Safe.')

# Implement method to ask the user if they have covid19 before shopping as a health and safety protocol
def health_and_safety(Covid19):
    while True:
        if Covid19 == 'yes':
            print('Please do not try and collect you items from your local store. Please call 090 123 4567 and give your address to the operator and we will deliver your order to you. Stay safe and feel better.')
            break
        else:
            print('Please feel free to either collect your items from your local store or call 090 123 4567 and give your address to the operator and we will deliver your order to you. Stay safe and feel better.')
            break

# Implement method so that the user gets a Welcome message from our store before shopping
def welcome(Active_Hunter):
    print('Hello valued customer and welcome Active Hunter, the store that offers almost everything and anything that you can think of. The one catch is that you\'ve to hunt for what you want before someone else gets to it first.')
    print('Due to the current Covid19 epidemic we would like to ask you a few questions just in case you come into our store such so that contact tracing is easier.')
    print('We at Active Hunter apologize for the inconvenience but we want to make sure that all of our valued staff and customers are as safe as possible.')
    print('If you are one of our esteemed loyal customers please enter your loyalty card number in order so see what special offers we have for you this week, especially with the holidays right around the corner')
    print('If you are joining us for the first time please take a look at our current sales and we look forward to seeing you again')

# Main Program itself
welcome_speech = 0
# prompt and read the customers name
customer_name = str(input('Enter customer\'s name: '))
# prompt the date
current_date = str(input('Enter today\'s date: '))
# prompt for covid
Covid19 = str(input('Do you have symptoms of Covid19 or have you been in contact with someone with Covid19 yes / no: '))
# print the name and date
print('Customer name:', customer_name, end='\n')
print('Today\'s date:', current_date, end='\n')
# call the class with the parameters
newCart = ShoppingCart(customer_name, current_date)
# welcome from the store founder Mr.Hunter god bless him during these tough times
welcome(welcome_speech)
# prompt for covid19 symptoms before the customer begins their order
health_and_safety(Covid19)
# print the details.
print_menu(newCart)
