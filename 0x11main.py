#Milestone Project 2: Mini Shopping Cart System

cart = {}

print("Welcome to MiniMart!")
print("1. Add item to cart")
print("2. Remove item from cart")
print("3. View cart")
print("4. Checkout")

while True:
    choice = input("Choose an option: ")

    if choice == "1":
        item = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        cart[item] = cart.get(item, 0) + quantity
        print(f"{item} added to cart.")

    elif choice == "2":
        item = input("Enter item name to remove: ")
        if item in cart:
            del cart[item]
            print(f"{item} removed from cart.")
        else:
            print(f"{item} not found in cart.")

    elif choice == "3":
        if not cart:
            print("Your cart is empty.")
        else:
            print("Your cart contains:")
            print(cart)

    elif choice == "4":
        print("Thank you for shopping! You bought:")
        if not cart:
            print("Nothing (your cart was empty).")
        else:
            print(cart)

    else:
        print("Invalid option. Please choose 1-4.")

    print("-----")
    print("-----")