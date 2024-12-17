x = int(input("Please enter a number: "))
y = int(input("Please enter a different number: "))
z = int(input("Please enter a another number: "))

if x > y and x > z:
    print("The largest number is ", x)
elif y > x and y > z:
    print("The largest number is ", y)
else:
    print("The largest number is ", z)



if 