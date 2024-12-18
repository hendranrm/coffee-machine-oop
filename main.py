from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# coffee menu obj
coffee_menu = Menu()

# coffee maker obj
coffee_machine_operation = CoffeeMaker()

# payment obj
payment_machine = MoneyMachine()

# set machine off button to false
machine_off = False

while not machine_off:
    # ask user their drink
    user_input = input(f'What would you like to drink?, we have {coffee_menu.get_items()}')

    # off button
    if user_input == 'off':
        machine_off = True
    
    # report button
    elif user_input == 'report':
        coffee_machine_operation.report()
        payment_machine.report()
    
    # evaluating user input
    elif user_input == 'latte' or 'cappucino' or 'espresso':
        for item in coffee_menu.menu:
            if item.name == user_input:
                check_resources_available = coffee_machine_operation.is_resource_sufficient(item)
                if check_resources_available == True:
                   print(f'The price of your {user_input} is {item.cost}')
                   payment_success = payment_machine.make_payment(item.cost)
                   if payment_success:
                       coffee_machine_operation.make_coffee(item)
                       
                       
                       
                       
                   
