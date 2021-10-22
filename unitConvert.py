num1= float( input("Enter the Value to convert: "))
print("You can enter the unit - m, km, yd, in, ft\n")
unit1 = input('Which unit do you want it converted from: ')
unit2 = input('Which unit do you want it converted to: ')

if unit1 == "m" and unit2 == "yd":
    ans = num1 * 1.09361
    print(ans)

elif unit1 == "m" and unit2 == "in":
    ans = num1 * 39.37
    print(ans)

elif unit1 == "m" and unit2 == "ft":
    ans = num1 *  3.281
    print(ans)

elif unit1 == "m" and unit2 == "km":
    ans = num1 / 1000
    print(ans)

elif unit1 == "yd" and unit2 == "m":
    ans = num1 / 1.094
    print(ans)

elif unit1 == "yd" and unit2 == "in":
    ans = num1 * 36
    print(ans)

elif unit1 == "yd" and unit2 == "ft":
    ans = num1 * 3
    print(ans)

elif unit1 == "yd" and unit2 == "km":
    ans = num1 * 0.0009144
    print(ans)

elif unit1 == "in" and unit2 == "m":
    ans = num1 / 39.37
    print(ans)

elif unit1 == "in" and unit2 == "yd":
    ans = num1 / 36
    print(ans)

elif unit1 == "in" and unit2 == "ft":
    ans = num1 / 12
    print(ans)

elif unit1 == "in" and unit2 == "km":
    ans = num1 / 39370
    print(ans)

elif unit1 == "ft" and unit2 == "m":
    ans = num1 / 3.281
    print(ans)

elif unit1 == "ft" and unit2 == "yd":
    ans = num1 / 3
    print(ans)

elif unit1 == "ft" and unit2 == "in":
    ans = num1 * 12
    print(ans)

elif unit1 == "ft" and unit2 == "km":
    ans = num1 / 3281
    print(ans)

elif unit1 == "km" and unit2 == "m":
    ans = num1 * 1000
    print(ans)

elif unit1 == "km" and unit2 == "yd":
    ans = num1 * 1094
    print(ans)

elif unit1 == "km" and unit2 == "in":
    ans = num1 * 39370
    print(ans)

elif unit1 == "km" and unit2 == "ft":
    ans = num1 * 3281
    print(ans)
