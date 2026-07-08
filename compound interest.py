#compound interest
principle=0
interest=0
time=0
while principle<=0:
    principle=float(input("enter the principle amount"))
    if principle<0:
        print("principle can not be zero")
    else:
        break
while interest<=0:
    interest=float(input("enter the interest"))
    if interest<0:
        print("interest can not be zero")
    else:
        break
while time<=0:
    time=float(input("enter the time"))
    if time<0:
        print("time can not be zero")
    else:
        break
print(principle)
print(interest)
print(time)
Amount=principle*pow(1+(interest/100),time)
print(Amount)