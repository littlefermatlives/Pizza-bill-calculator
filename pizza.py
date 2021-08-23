a = input(("Choose the size of pizza you want: S , M or L "))
b = input(("Do you want to add pepperoni to it? Y or N "))
c = input("Do you want to add extra cheese to it? Y or N ")
bill = 0
if a == "S":
    bill += 100
elif a == "M":
    bill += 200
else:
    bill += 300
if b == "Y":
    bill += 70
if c == "Y":
    bill += 50
print(f"Your total bill is {bill}")
print("Thank You")