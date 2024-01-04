import random
import math

class Pizzas:

   # Created constructor with required parameters   
   def __init__(self, MenuCode, MenuName, PizzaCount):
     self.MenuCode = MenuCode
     self.MenuName = MenuName
     self.PizzaCount = PizzaCount
            
   def getValue(self, PizzaCount): 
    # The price random variable
    price = random.randint(1, 10)
    # Made price into a float to display the 2 decimal points
    price = float(price)
    total = PizzaCount * price
    print(total)

   
   def toString(self, MenuCode, MenuName, PizzaCount, getValue):
      return f"""
Listed below is your current pizza inventory:
Menu Code: {MenuCode}
Menu Name: {MenuName}
Total Pizza Count: {PizzaCount}
Total Inventory Cost: {getValue}
      """


########################
########################
#DRIVER SECTION
      #Enter your code below
# Named IQE which stands for Item Quantality Entry, which is the first step
IQE = input("""How many simulated frozen pizza items do you want to create? You must enter between 1 and 10
""")

# Confirmation of IQE
Response1 = print(f"You entered: {IQE}")

# Step 2, which will be three letter code entry, abbreviated to TLCE
Pizzas.MenuCode = input("""You will now create the menu item code for the invevory management system,
name of the menu item and how much inventory for the pizza to keep in the freezer.
The price will be randomly generated.


Please enter a three letter/number menu code for pizza number 1:             
""")

# Program will now proceed with step 3, giving feedback to step 2 and asking user to enter name of each pizza item, variable will be abbreviated to PNE for Pizza Name Entry
Response2 = print(f"You entered: {Pizzas.MenuCode}")
Pizzas.MenuName = input("""Please enter the pizza name            
""")
#Step 4, asks user storage quantity to keep in the freezer, abbreviated to SQ
Pizzas.PizzaCount = input(f"""Please enter total inventory count of this {Pizzas.MenuName} pizza to keep in the freezer:
""")
