unit=int(input("enter the number"))
if unit <=50:
    print("cost",unit*0.50)
elif unit>=50  and unit<=150:
    print("cost",unit*0.75)
elif unit>=150 and unit<=250:
    print("cost",unit*1.20)
else:
    print("cost",unit*1.50)        