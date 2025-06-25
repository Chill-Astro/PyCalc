#!/usr/bin/env python3
import os
import requests
import math as mt
appName = "PyCalc"
appVer = "1.8" # Resaissance
rawGistURL = "https://gist.githubusercontent.com/Chill-Astro/e8c32d9a2b30780e3b6fd2819a51b330/raw/PyC_V.txt"
# Ensure config file exists
if not os.path.exists("PyC_Conf.txt"):
    with open("PyC_Conf.txt", "w") as f:
        f.write("// PyCalc Configuration for Update Check.\ntrue\ntrue\n")  # Default values
# Read first line to check for first run
with open("PyC_Conf.txt", "r") as f:
    lines = f.readlines()
first_line = lines[1].strip() if len(lines) > 1 else "true"
update_check = lines[2].strip() if len(lines) > 2 else "true"

if first_line == "true":
    uch = input("Do you want to enable update check? [y/n] : ").strip().lower()
    new_line = "true\n" if uch == "y" else "false\n"
    # Set first line to false, third line to user's choice
    lines = [lines[0] if len(lines) > 0 else "// PyCalc Configuration for Update Check.\n", "false\n", new_line]
    with open("PyC_Conf.txt", "w") as f:
        f.writelines(lines)
    print()
    update_check = new_line.strip()

def update(appVer, appName, gistURL, check):
    try:
        response = requests.get(gistURL, timeout=5) # Fetch version file, timeout after 5 seconds
        response.raise_for_status()  # Raise an error for bad responses
        newVer = response.text.strip()  # Get the version from the response
        if check == "true":
            if newVer > appVer:
                print(f"Update Available : v{newVer}\n")
            elif newVer == appVer:
                print("Up to date\n") # Latest Version
            elif newVer < appVer:
                print(f"DEV. Build\n") # For development builds
        else:
            print(f"Update check Disabled.\n")
    except requests.RequestException as e:
        print("⚠️  Could not check for updates. Please check your internet connection.\n" f"Error: {e}\n")
    except Exception as e: # Catching other potential errors, like if the content of the file is not proper.
        print("⚠️  Error occurred while checking for updates.\n" f"Error: {e}\n")
def perform_binary_operation(operator, operation_func):
    try:
        x = float(input("Enter first number : "))
        print()
        y = float(input("Enter second number : "))
        print()
        print(f"{x} {operator} {y} = {operation_func(x, y)}\n")
    except ValueError:
        print("Invalid input. Please enter numbers only.\n")

if update_check == "true":
    update(appVer, appName, rawGistURL, update_check)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def basic_math_menu():
    while True:
        clear_screen()
        print("Select an Operation :\n\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponents (x^y)\n6. Square Root\n7. Cube Root\n8. Exit to Main Menu\n")
        ch = input("Enter choice [ 1 - 8 ] : ")
        print()
        if ch == '1':
            perform_binary_operation("+", lambda a, b: a + b)
        elif ch == '2':
            perform_binary_operation("-", lambda a, b: a - b)
        elif ch == '3':
            perform_binary_operation("*", lambda a, b: a * b)
        elif ch == '4':
            try:
                x = float(input("Enter first number : "))
                print()
                y = float(input("Enter second number : "))
                print()
                if y == 0:
                    print("Div. by Zero Not Defined!\n")
                else:
                    print(f"{x} / {y} = {x / y}\n")
            except ValueError:
                print("Invalid input. Please enter numbers only.\n")
        elif ch == '5':
            perform_binary_operation("^", mt.pow)
        elif ch == '6':
            x = float(input("Enter a number : "))
            print()
            print(f"Root x =  {mt.sqrt(x)}\n")
        elif ch == '7':
            x = float(input("Enter a number : "))
            print()
            print(f"C. Root x =  {mt.cbrt(x)}\n")
        elif ch == '8':
            clear_screen()
            return
        else:
            print("Invalid input!\n")
        input("Press Enter to continue...")

def mensuration_menu():
    while True:
        clear_screen()
        print("Select an Operation :\n\n1. Perimeter [Various Shapes]\n2. Area [Various Shapes]\n3. Volume [Various Shapes]\n4. Surface Area [Various Shapes]\n5. Curved Surface Area [Various Shapes]\n6. Diagonal Calculation [Various Shapes]\n7. Exit to Main Menu\n")
        ch = input("Enter choice [ 1 - 7 ] : ")
        print()
        if ch == '1':
            while True:
                print("\nSelect a shape : \n\n1. Equilateral Triangle\n2. Isosceles Triangle\n3. Square / Rhombus\n4. Rectangle / Parallelogram\n5. Circle\n6. Back\n")
                sch = input("Enter shape choice [ 1 - 6 ] : ")
                print()
                match sch:
                    case '1':
                        a = float(input("Enter Side Length [a] : "))
                        print()
                        print(f"Perimeter :  {3*a}\n")
                        input("Press Enter to continue...")
                    case '2':
                        a = float(input("Enter Equal Side's Length : "))
                        print()
                        b = float(input("Enter Non-Equal Side's Length : "))
                        print()
                        print(f"Perimeter :  {2*a+b}\n")
                        input("Press Enter to continue...")
                    case '3':
                        a = float(input("Enter Length of Side [a] : "))
                        print()
                        print(f"Perimeter :  {4*a}\n")
                        input("Press Enter to continue...")
                    case '4':
                        l = float(input("Enter Length of Rectangle / Parallelogram [l] : "))
                        print()
                        b = float(input("Enter Breadth of Rectangle / Parallelogram [l] : "))
                        print()
                        print(f"Perimeter :  {2*(l + b)}\n")
                        input("Press Enter to continue...")
                    case '5':
                        r = float(input("Enter the Radius [r] : "))
                        print()
                        c = 2*mt.pi*r
                        print(f"Circumference :  {c}\n")
                        input("Press Enter to continue...")
                    case '6':
                        break
                    case _:
                        print("Invalid Option! Exiting Perimeter Calculation ...\n")
                        input("Press Enter to continue...")
        elif ch == '2':
            while True:
                print("\nSelect a shape : \n1. Equilateral Triangle\n2. Isosceles Triangle\n3. Square\n4. Rectangle / Parallelogram\n5. Rhombus\n6. Circle\n7. Semi-circle\n8. Back\n")
                sch = input("Enter shape choice [ 1 - 8 ] : ")
                print()
                match sch:
                    case '1':
                        a = float(input("Enter Side Length [a] : "))
                        print()
                        ar = (mt.sqrt(3) / 4) * mt.pow(a, 2)
                        print(f"Area :  {ar}\n")
                        input("Press Enter to continue...")
                    case '2':
                        a = float(input("Enter Equal Side's Length : "))
                        print()
                        b = float(input("Enter Non-Equal Side's Length : "))
                        print()
                        ar = mt.sqrt(4*mt.pow(a, 2) - mt.pow(b, 2)) / 4
                        print(f"Area :  {ar}\n")
                        input("Press Enter to continue...")
                    case '3':
                        a = float(input("Enter Length of Side [a] : "))
                        print()
                        ar = mt.pow(a, 2)
                        print(f"Area :  {ar}\n")
                        input("Press Enter to continue...")
                    case '4':
                        l = float(input("Enter Length of Rectangle / Parallelogram [l] : "))
                        print()
                        b = float(input("Enter Breadth of Rectangle / Parallelogram [l] : "))
                        print()
                        ar = l * b
                        print(f"Area :  {ar}\n")
                        input("Press Enter to continue...")
                    case '5':
                        d1 = float(input("Enter Diagonal 1 [d1] : "))
                        print()
                        d2 = float(input("Enter Diagonal 2 [d2] : "))
                        print()
                        area = 0.5 * d1 * d2
                        print(f"Area of Rhombus :  {area}\n")
                        input("Press Enter to continue...")
                    case '6':
                        r = float(input("Enter the Radius [r] : "))
                        print()
                        area = mt.pi * mt.pow(r, 2)
                        print(f"Area :  {area}\n")
                        input("Press Enter to continue...")
                    case '7':
                        r = float(input("Enter the Radius [r] : "))
                        print()
                        area = 0.5 * mt.pi * mt.pow(r, 2)
                        print(f"Area :  {area}\n")
                        input("Press Enter to continue...")
                    case '8':
                        break
                    case _:
                        print("Invalid Option! Exiting Area Calculation ...\n")
                        input("Press Enter to continue...")
        elif ch == '3':
            while True:
                print("\nSelect a shape : \n"  "1. Cube\n" "2. Cuboid\n" "3. Cylinder\n" "4. Cone\n" "5. Sphere\n6. Back\n")
                sch = input("Enter shape choice [ 1 - 6 ] : ")
                print()
                match sch:
                    case '1': # Cube
                        a = float(input("Enter Length of Side [a] : "))
                        print()
                        vol = mt.pow(a, 3)
                        print(f"Volume :  {vol}\n")
                        input("Press Enter to continue...")
                    case '2': # Cuboid
                        l = float(input("Enter Length [l] : "))
                        print()
                        b = float(input("Enter Breadth [b] : "))
                        print()
                        h = float(input("Enter Height [h] : "))
                        print()
                        vol = l * b * h
                        print(f"Volume :  {vol}\n")
                        input("Press Enter to continue...")
                    case '3': # Cylinder
                        r = float(input("Enter the Radius [r] : "))
                        print()
                        h = float(input("Enter the Height [h] : "))
                        print()
                        vol = mt.pi * mt.pow(r, 2) * h
                        print(f"Volume :  {vol}\n")
                        input("Press Enter to continue...")
                    case '4': # Cone
                        r = float(input("Enter the Radius [r] : "))
                        print()
                        h = float(input("Enter the Height [h] : "))
                        print()
                        vol = (1/3) * mt.pi * mt.pow(r, 2) * h
                        print(f"Volume :  {vol}\n")
                        input("Press Enter to continue...")
                    case '5': # Sphere
                        r = float(input("Enter the Radius [r] : "))
                        print()
                        vol = (4/3) * mt.pi * mt.pow(r, 3)
                        print(f"Volume :  {vol}\n")
                        input("Press Enter to continue...")
                    case '6':
                        break
                    case _:
                        print("Invalid Option! Exiting Volume Calculation ...\n")
                        input("Press Enter to continue...")
        elif ch == '4' : # Surface Area [Various Shapes]
            while True:
                print("\nSelect a shape : \n" "1. Cube\n" "2. Cuboid\n" "3. Cylinder\n" "4. Cone\n" "5. Sphere\n6. Back\n")
                sch = input("Enter shape choice [ 1 - 6 ] : ")
                print()
                match sch:
                    case '1': # Cube
                        a = float(input("Enter Length of Side [a] : "))
                        print()
                        sa = 6 * mt.pow(a, 2)
                        print(f"Surface Area :  {sa}\n")
                        input("Press Enter to continue...")
                    case '2': # Cuboid
                        l = float(input("Enter Length [l] : "))
                        print()
                        b = float(input("Enter Breadth [b] : "))
                        print()
                        h = float(input("Enter Height [h] : "))
                        print()
                        sa = 2 * (l * b + b * h + h * l)
                        print(f"Surface Area :  {sa}\n")
                        input("Press Enter to continue...")
                    case '3': # Cylinder
                        r = float(input("Enter the Radius [r] : "))
                        print()
                        h = float(input("Enter the Height [h] : "))
                        print()
                        sa = 2 * mt.pi * r * (r + h)
                        print(f"Surface Area :  {sa}\n")
                        input("Press Enter to continue...")
                    case '4': # Cone
                        r = float(input("Enter the Radius [r] : "))
                        print()
                        h = float(input("Enter the Height [h] : "))
                        print()
                        sa = mt.pi * r * (r + mt.sqrt(mt.pow(h, 2) + mt.pow(r, 2)))
                        print(f"Surface Area :  {sa}\n")
                        input("Press Enter to continue...")
                    case '5': # Sphere
                        r = float(input("Enter the Radius [r] : "))
                        print()
                        sa = 4 * mt.pi * mt.pow(r, 2)
                        print(f"Surface Area :  {sa}\n")
                        input("Press Enter to continue...")
                    case '6':
                        break
                    case _:
                        print("Invalid Option! Exiting Surface Area Calculation ...\n")
                        input("Press Enter to continue...")
        elif ch == '5' : # Curved Surface Area [Various Shapes]
            while True:
                print("\nSelect a shape : \n" "1. Cylinder\n" "2. Cone\n" "3. Sphere\n6. Back\n")
                sch = input("Enter shape choice [ 1 - 3 ] : ")
                print()
                match sch:
                    case '1': # Cylinder
                        r = float(input("Enter the Radius [r] : "))
                        print()
                        h = float(input("Enter the Height [h] : "))
                        print()
                        csa = 2 * mt.pi * r * h
                        print(f"Curved Surface Area :  {csa}\n")
                        input("Press Enter to continue...")
                    case '2': # Cone
                        r = float(input("Enter the Radius [r] : "))
                        print()
                        h = float(input("Enter the Height [h] : "))
                        print()
                        csa = mt.pi * r * mt.sqrt(mt.pow(h, 2) + mt.pow(r, 2))
                        print(f"Curved Surface Area :  {csa}\n")
                        input("Press Enter to continue...")
                    case '3': # Sphere
                        r = float(input("Enter the Radius [r] : "))
                        print()
                        csa = 2 * mt.pi * mt.pow(r, 2)
                        print(f"Curved Surface Area :  {csa}\n")
                        input("Press Enter to continue...")
                    case '6':
                        break
                    case _:
                        print("Invalid Option! Exiting Curved Surface Area Calculation ...")
                        input("Press Enter to continue...")
        elif ch == '6': # Diagonal Calculation [Various Shapes]
            while True:
                print("Diagonal Calculation [Various Shapes]\n"
                      "Select a shape : \n" "1. Square\n" "2. Rectangle\n" "3. Cube\n" "4. Cuboid\n5. Back\n")
                sch = input("Enter shape choice [ 1 - 5 ] : ")
                print()
                match sch:
                    case '1': # Square
                        a = float(input("Enter Length of Side [a] : "))
                        print()
                        d = mt.sqrt(2) * a
                        print(f"Diagonal :  {d}\n")
                        input("Press Enter to continue...")
                    case '2': # Rectangle
                        l = float(input("Enter Length [l] : "))
                        print()
                        b = float(input("Enter Breadth [b] : "))
                        print()
                        d = mt.sqrt(mt.pow(l, 2) + mt.pow(b, 2))
                        print(f"Diagonal :  {d}\n")
                        input("Press Enter to continue...")
                    case '3': # Cube
                        a = float(input("Enter Length of Side [a] : "))
                        print()
                        d = mt.sqrt(3) * a
                        print(f"Diagonal :  {d}\n")
                        input("Press Enter to continue...")
                    case '4': # Cuboid
                        l = float(input("Enter Length [l] : "))
                        print()
                        b = float(input("Enter Breadth [b] : "))
                        print()
                        h = float(input("Enter Height [h] : "))
                        print()
                        d = mt.sqrt(mt.pow(l, 2) + mt.pow(b, 2) + mt.pow(h, 2))
                        print(f"Diagonal :  {d}\n")
                        input("Press Enter to continue...")
                    case '5':
                        break
                    case _:
                        print("Invalid Option! Exiting Diagonal Calculation ...")
                        input("Press Enter to continue...")
        elif ch == '7': # Exit to Main Menu
            clear_screen()
            return
        else:
            print("Invalid input!\n")
        input("Press Enter to continue...")

def finance_menu():
    while True:
        clear_screen()
        print("Select an Operation :\n\n1. Simple Interest\n2. Compound Interest\n3. Exit to Main Menu\n")
        ch = input("Enter choice [ 1 - 3 ] : ")
        if ch == '1':
            p = float(input("Enter the Principal : "))
            print()
            r = float(input("Enter the Rate [ % ] : "))
            print()
            t = float(input("Enter the Time [ Years ] : "))
            print()
            si = p * r * t / 100
            print(f"Simple Interest :  {si}\nAmount :  {(si + p)}\n")
        elif ch == '2':
            print("Compound Interest Calculation\n")
            p = float(input("Enter the Principal : "))
            print()
            r = float(input("Enter the Rate [ % ] : "))
            print()
            n = float(input("Enter the number of times interest is compounded per year : "))
            print()
            t = float(input("Enter the Time [ Years ] : "))
            print()
            a = p * mt.pow((1 + r / (100 * n)), n * t)
            ci = a - p
            print(f"Compound Interest :  {ci}\nAmount :  {a}\n")
        elif ch == '3':
            clear_screen()
            return
        else:
            print("Invalid input!\n")
        input("Press Enter to continue...")

def extras_menu():
    while True:
        clear_screen()
        print("Select an Operation :\n\n1. Approximate / Rounding\n2. Prime No. Check\n3. Triangle Check\n4. Right Triangle Check\n5. Factorial Calculator\n6. Exit to Main Menu\n")
        ch = input("Enter choice [ 1 - 6 ]: ")
        print()
        if ch == '1':
            x = float(input("Enter a number : "))
            print()
            print(f"{round(x)}\n")
        elif ch == '2':
            x = int(input("Enter a Number : "))
            print()
            if x > 1:
                for i in range(2, x):
                    if (x % i) == 0:
                        print(f"{x} is not a Prime Number\n")
                        break
                else:
                    print(f"{x} is a Prime Number\n")
            else:
                print(f"{x} is not a Prime Number\n")
        elif ch == '3':
            a = float(input("Enter first side [a] : "))
            print()
            b = float(input("Enter second side [b] : "))
            print()
            c = float(input("Enter third side [c] : "))
            print()
            if(a <= 0 or b <= 0 or c <= 0):
                print("Sides must be +ve\n")
            elif (a + b > c) and (a + c > b) and (b + c > a):
                print("Valid Triangle\n")
            else:
                print("Not a Valid Triangle\n")
        elif ch == '4':
            a = float(input("Enter first side [a] : "))
            print()
            b = float(input("Enter second side [b] : "))
            print()
            c = float(input("Enter third side [c] : "))
            print()
            if(a <= 0 or b <= 0 or c <= 0):
                print("Sides must be +ve\n")
            elif(mt.pow(a,2) + mt.pow(b,2) == mt.pow(c,2)) or (mt.pow(a,2) + mt.pow(c,2) == mt.pow(b,2)) or (mt.pow(b,2) + mt.pow(c,2) == mt.pow(a,2)):
                print("Is a Right Triangle\n")
            else:
                print("Not a Right Triangle.\n")
        elif ch == '5':
            x = int(input("Enter a Number : "))
            print()
            if x < 0:
                print("\nFactorial Not Defined for Negative Numbers!\n")
            elif x == 0 or x == 1:
                print(f"\nFactorial of {x} is 1\n")
            else:
                fact = 1
                for i in range(2, x + 1):
                    fact *= i
                print(f"\nFactorial of {x} is {fact}\n")
        elif ch == '6':
            clear_screen()
            return
        else:
            print("Invalid input!\n")
        input("Press Enter to continue...")

def update_check_menu():
    # Toggle update check setting in config file
    with open("PyC_Conf.txt", "r") as f:
        lines = f.readlines()
    if len(lines) < 3:
        while len(lines) < 3:
            lines.append("true\n")
    current = lines[2].strip()
    if current == "true":
        lines[2] = "false\n"
        print("Update check has been disabled.\n")
    else:
        lines[2] = "true\n"
        print("Update check has been enabled.\n")
    with open("PyC_Conf.txt", "w") as f:
        f.writelines(lines)
    input("Press Enter to return to Main Menu...")
    clear_screen()

def main_menu():
    while True:
        clear_screen()
        print(f"{appName} v{appVer} - Status : ", end="")
        # Read update_check from config each time in case it was changed
        with open("PyC_Conf.txt", "r") as f:
            lines = f.readlines()
            update_check = lines[2].strip() if len(lines) > 2 else "true"
        check = ""
        if update_check == "true":
            check = "true"
        update(appVer, appName, rawGistURL, check)
        print("Select a Mode :\n\n1. Basic Maths\n2. Mensuration\n3. Finance\n4. Extras\n5. Enable / Disable Update Check\n6. Exit PyCalc\n")
        ch = input("Enter choice [ 1 - 6 ] : ")
        print()
        if ch == '1':
            basic_math_menu()
        elif ch == '2':
            mensuration_menu()
        elif ch == '3':
            finance_menu()
        elif ch == '4':
            extras_menu()
        elif ch == '5':
            update_check_menu()
        elif ch == '6':            
            exit(0)
        else:
            print("Invalid input!\n")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main_menu()