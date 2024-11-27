name = input("Kindly! Enter the Name:-").title()
message = f"Welcome {name} to the Personalised Tourist Guide"
print(message)

def get_destination():
    while True:
        destination = input("Where do you want to go\n1.mountains\n2.beach\n ").strip().lower()
        if destination == "mountains":
            print("You have selected mountains")
            break
        elif destination == "beach":
            print("You have selected beach")
            break
        else:
            print("Please Enter valid Input ")    

get_destination() 


def get_budget():
    while True:
        budget = int (input("Enter the budget"))
        if budget >= 500:
            print("Luxury")
            break
        elif budget >= 200:
            print("Budget freindly")
            break
        elif budget <0:
            print("You have entered Invalid input")
        else:
            break
    return budget

budget = get_budget()  

def totalCost(budget,days):
    return budget* days

def getValidNumOfDays(prompt):
    while True:
        try:
            days = int(input(prompt))
            return days
        except ValueError:
            print("Invalid Input!, Enter again ")

days = getValidNumOfDays("Enter number of days: ")

totalCost = totalCost(budget,days)

print(f"No of days is - {days}\nYour Budget is - {budget}\nTotalCost of the trip - {totalCost}")