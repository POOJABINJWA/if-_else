a=int(input("enter the angle1"))
b=int(input("enter the angle2"))
c=int(input("enter the angle3"))
if a==90 or b==90 or c==90:
    print("this is right angle tringle")
elif a<90 or b<90 or c<90:
    print("this is actue angle tringle")
elif a>90 or b>90 or c>90:
    print("this is outuse andle tringle")
else:
    print("none")     
       