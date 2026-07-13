#concession stand
menu={"biryani":100,
      "soda":20,
      "drink":40,
      "ice":40,
      "chicken":330 }
      
cart=[]
total=0
print("--------------------// Menu Card //------------------------")
for key,value in menu.items():
    print(f"{key} : {value}")
while True:
    food=input("Enter the food item (not q):")
    print(f"The food item is {food}")
    cost=menu.get(food)
    print(f"the cost of the item is : {cost}")
    if food=="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("--------------------//My Cart//------------------------")
for food in cart:
    print(food, end=" ")
    total=total+menu.get(food)
print()
print(f"The total amount is {total}")