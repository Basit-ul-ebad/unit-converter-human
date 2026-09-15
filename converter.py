# Unit Converter
# my python project
# converts length, weight and temperature

print("==============================")
print("   WELCOME TO UNIT CONVERTER  ")
print("==============================")


def length():
    print("units: m, km, cm, mm, inch, ft, mile")
    value = float(input("Enter value: "))
    frm = input("From unit: ")
    to = input("To unit: ")

    # first change everything to meter
    if frm == "m":
        meter = value
    elif frm == "km":
        meter = value * 1000
    elif frm == "cm":
        meter = value / 100
    elif frm == "mm":
        meter = value / 1000
    elif frm == "inch":
        meter = value * 0.0254
    elif frm == "ft":
        meter = value * 0.3048
    elif frm == "mile":
        meter = value * 1609.34

    # then meter to the other unit
    if to == "m":
        answer = meter
    elif to == "km":
        answer = meter / 1000
    elif to == "cm":
        answer = meter * 100
    elif to == "mm":
        answer = meter * 1000
    elif to == "inch":
        answer = meter / 0.0254
    elif to == "ft":
        answer = meter / 0.3048
    elif to == "mile":
        answer = meter / 1609.34

    print(value, frm, "=", answer, to)


def weight():
    print("units: kg, g, lb, oz")
    value = float(input("Enter value: "))
    frm = input("From unit: ")
    to = input("To unit: ")

    units = {"kg": 1, "g": 0.001, "lb": 0.4536, "oz": 0.02835}
    kg = value * units[frm]
    answer = kg / units[to]
    print(value, frm, "=", answer, to)


def temperature():
    print("units: C, F, K")
    value = float(input("Enter temperature: "))
    frm = input("From (C/F/K): ")
    to = input("To (C/F/K): ")

    if frm == to:
        answer = value
    elif frm == "C" and to == "F":
        answer = value * 9 / 5 + 32
    elif frm == "F" and to == "C":
        answer = (value - 32) * 5 / 9
    elif frm == "C" and to == "K":
        answer = value + 273.15
    elif frm == "K" and to == "C":
        answer = value - 273.15
    elif frm == "F" and to == "K":
        answer = (value - 32) * 5 / 9 + 273.15
    elif frm == "K" and to == "F":
        answer = (value - 273.15) * 9 / 5 + 32

    print(value, frm, "=", answer, to)


def main():
    print()
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    print("4. Exit")
    choice = int(input("Choose option: "))

    if choice == 1:
        length()
    elif choice == 2:
        weight()
    elif choice == 3:
        temperature()
    elif choice == 4:
        print("Bye!")
        return
    else:
        print("Wrong option")

    again = input("Do you want to convert again? (y/n): ")
    if again == "y":
        main()
    else:
        print("Bye!")


main()
