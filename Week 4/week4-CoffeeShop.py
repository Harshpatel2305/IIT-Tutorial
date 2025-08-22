print("welcome to the coffee shop")

customerName = input("enter your name:")
print("hello ",customerName)

coffeePrice = 3.50
lattePrice = 4.50
mochaPrice = 5.50

print("coffe price is ",coffeePrice)
print("latte price is ",lattePrice)
print("mocha price is ",mochaPrice)



cost = 0

userChoice = input("what would you like to order?:-")

while True:
    match userChoice:
        case "coffee":
            cost += coffeePrice
        case "latte":
            cost += lattePrice
        case "mocha":
            cost += mochaPrice
        case _:
            print("invalid choice")
    
    quantity = int(input("how many would you like to order?:-"))
    cost = cost * quantity
    choice = input("would you like to order anything else? (yes/no):-")
    if choice.lower() == "yes":
        userChoice = input("what would you like to order?:-")
    elif choice.lower() == "no":
        break
    else:
        print("invalid choice, please enter yes or no")
        continue
    


print("your total cost is ",cost)

isStudent = input("are you a student?:-")

if isStudent == "yes":
    cost = cost - cost*0.1

print("your total cost is ",cost)
print("thank you for visiting the coffee shop")






