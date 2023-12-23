Weight = int(input("Enter your weight in 'kg': "))
unit = input("Enter L for 'lbs' or G for 'gram': ")
if unit.upper() == 'L':
    print(Weight * 0.45)
elif unit.upper() == 'G':
    print(Weight * 1000)
else:
    print('You can check the Weight only in lbs or grams')