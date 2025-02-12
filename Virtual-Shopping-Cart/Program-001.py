name = input("Kindly!! Enter the Name").title()
print(f"Hello {name} Welcome to this Virtual Shopping Cart")

mobno = int(input("Enter the Mobile no"))
def getQuantity():
    while True:
        try:
            quantity = int(input("Enter the quantity of the item: "))
            if quantity <=0:
                print("Quantity must be positive integer")
            else:
                return quantity
        except ValueError:
            print("Invalid Quantity")

def display(cart):
    print("Items in Your Cart:")
    for item, quantity in cart.items():
        print(f"{item}: {quantity}")

def totalCost(cart, price):
    total = 0
    for item, quantity in cart.items():
        total += price[item] * quantity
    return total

def applyDiscount(total):
    discount = total * 0.1
    return total - discount

def checkout(cart, price):
    print(f"Thankyou for shopping from our cart {name} sir ")
    print(f"Contact Details {mobno}")
    display(cart)
    total = totalCost(cart, price)
    print(f"{total:.2f} before discount")
    total = applyDiscount(total)
    print(f"Your final total is: {total:.2f}")
    return total

def main():
    print("Welcome to the shopping cart. Select items")
    items = ['Apples', 'Mosambi', 'Banana', 'Anar', 'Aam']
    price = {'Apples': 20, 'Anar': 33.5, 'Aam': 45.6, 'Mosambi': 40, 'Banana': 10}  # added price for Banana
    cart = {}
    while True:
        print("Available Items: ")
        for i in items:
            print(i)
        choice = input('Enter item name: or Done if it is finished: ').capitalize().strip()
        if choice == 'Done':
            break
        elif choice in items:
            quantity = getQuantity()
            if choice in cart:
                cart[choice] += quantity
                print(f"{choice} updated by {quantity}")
            else:
                cart[choice] = quantity
                print("item added")
        else:
            print("Item not available ")
    if cart:
        checkout(cart, price)
    else:
        print('Empty Cart')

main()