#shopping cart
foods=[]
prices=[]
total=0
while True:
    food=input("enter the food (not q):")
    if food=="q":
        break
    else:
        price=int(input(f"enter the price of {food}:"))
        foods.append(food)
        prices.append(price)
        total=price+total
print("-----------------My Cart---------------------")
print(f"The total amount is {total}")