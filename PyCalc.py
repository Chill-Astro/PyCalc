#!/usr/bin/env python3
import math as mt
import requests
UPDATE_VERSION_URL = "https://gist.githubusercontent.com/Chill-Astro/e8c32d9a2b30780e3b6fd2819a51b330/raw/PyC_V.txt"
CURRENT_VERSION = "1.5" # Linux Release + Installer & Winget Support
def check_for_updates() : # Entire Update Check Thingy
    try:
        response = requests.get(UPDATE_VERSION_URL, timeout=5) # Fetch version file, timeout after 5 seconds
        response.raise_for_status() # Raise HTTPError for bad responses
        latest_version = response.text.strip() # Get version string from file and remove whitespace
        if latest_version > CURRENT_VERSION:
            print("--- UPDATE AVAILABLE! ---\n"
                  f"🎉 A NEW version of PyCalc is Available! : {latest_version}\n"
                  f"Currently using : {CURRENT_VERSION}\n"
                  "Please visit github.com/Chill-Astro/PyCalc to download the latest release!\n" # Provide URL for Updates
                  "-----------------------")
        elif latest_version == CURRENT_VERSION:
            print("🎉 PyCalc is up to date!")
        else:
            print("⚠️  This is a DEV. Build of PyCalc!\n") # For development scenarios
    except requests.exceptions.RequestException as e:
        print("--- UPDATE CHECK FAILED! ---\n"
              "⚠️ Could not check for updates. Please check your internet connection.\n"
              f"Error: {e}\n"
              "------------------------")
    except Exception as e: # Catching other potential errors, like if the content of the file is not proper
        print("--- UPDATE CHECK FAILED ---\n"
              "⚠️ Error occurred while checking for updates.\n"
              f"Error: {e}\n"
              "------------------------")
def perform_binary_operation(operator, operation_func):
    try:
        x = float(input("Enter first number : "))
        print()
        y = float(input("Enter second number : "))
        print()
        print(f"{x} {operator} {y} = {operation_func(x, y)}\n")
    except ValueError:
        print("Invalid input. Please enter numbers only.\n")
print("PyCalc : A Simple and Lightweight Calculator. Made in Python!\n" # Pycalc Starts here!
      f"Version : {CURRENT_VERSION}\n") # Print Version
check_for_updates() # Perform update check at startup
print("Select a Mathematical Operation : \n"
      "\n1. Addition\n" "2. Subtraction\n" "3. Multiplication\n" "4. Division\n" "5. Exponents (x^y)\n" "6. Square Root\n"
      "7. Cube Root\n" "8. Approximate / Rounding\n" "9. Heron's Formula\n" "10. Simple Interest\n" "11. Compound Interest\n" "12. Prime No. Check\n"
      "13. Triangle Check\n" "14. Right Triangle Check\n" "15. Perimiter [Various Shapes]\n" "16. Area [Varoius Shapes]\n"
      "17. Volume [Various Shapes]\n" "18. Surface Area [Various Shapes]\n" "19. Curved Surface Area [Various Shapes]\n"
      "20. Diagonal Calculation [Various Shapes]\n" "21. Factorial Calculator\n" "22. Exit PyCalc\n")
while True:
    ch = input("Enter choice [ 1 - 22 ] : ") # Input Choice
    print()
    match ch:
        case '1': # Addition
            perform_binary_operation("+", lambda a, b: a + b)

        case '2': # Subtraction
            perform_binary_operation("-", lambda a, b: a - b)

        case '3': # Multiplication
            perform_binary_operation("*", lambda a, b: a * b)

        case '4': # Division
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
        case '5': # Exponents
            perform_binary_operation("^", mt.pow)
        case '6': # Square Root
            x = float(input("Enter a number : "))
            print()
            print(f"Root x =  {mt.sqrt(x)}\n")
        case '7': # Cube Root
            x = float(input("Enter a number : "))
            print()
            print(f"C. Root x =  {mt.cbrt(x)}\n")
        case '8':  # Rounding
            x = float(input("Enter a number : "))
            print()
            print(f"{round(x)}\n")
        case '9': # Heron's Formula
            print("NOTE: Some Calculations may print 0.0 depending on the values!\n")
            a = float(input("Enter the first side [a] : "))
            print()
            b = float(input("Enter the second side [b] : "))
            print()
            c = float(input("Enter third side [c] : "))
            print()
            if(a <= 0 or b <= 0 or c <= 0): # Check for positive sides
                print("Sides must be +ve.\n")
                continue
            s = a + b + c
            print("Perimeter : ", s)
            s /= 2
            print("s =", s)
            ar = float(mt.sqrt(s * (s - a) * (s - b) * (s - c)))
            print("Area : ", ar)
            print()
        case '10': # Simple Interest
            p = float(input("Enter the Principal : "))
            print()
            r = float(input("Enter the Rate [ % ] : "))
            print()
            t = float(input("Enter the Time [ Years ] : "))
            print()
            si = p * r * t / 100
            print(f"Simple Interest :  {si}\nAmount :  {(si + p)}\n")
        case '11': # Compound Interest
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
        case '12' : # Prime Number Check
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
        case '13': # Triangle Check
            a = float(input("Enter first side [a] : "))
            print()
            b = float(input("Enter second side [b] : "))
            print()
            c = float(input("Enter third side [c] : "))
            print()
            if(a <= 0 or b <= 0 or c <= 0): # Check for positive sides
                print("Sides must be +ve\n")
                continue # Changed from 'break' to 'continue'
            elif (a + b > c) and (a + c > b) and (b + c > a):
                print("Valid Triangle\n")
            else:
                print("Not a Valid Triangle\n")
        case '14': # Right Triangle Check
            a = float(input("Enter first side [a] : "))
            print()
            b = float(input("Enter second side [b] : "))
            print()
            c = float(input("Enter third side [c] : "))
            print()
            if(a <= 0 or b <= 0 or c <= 0): # Check for positive sides
                print("Sides must be +ve\n")
                continue
            elif(mt.pow(a,2) + mt.pow(b,2) == mt.pow(c,2)) or (mt.pow(a,2) + mt.pow(c,2) == mt.pow(b,2)) or (mt.pow(b,2) + mt.pow(c,2) == mt.pow(a,2)): # Check all combinations for right triangle
                print("Is a Right Triangle\n")
            else:
                print("Not a Right Triangle.\n")
        case '15': # Perimeter [Various Shapes]
            print("Perimeter Calculation [Various Shapes]\n"
                  "Select a shape : \n" "1. Equilateral Triangle\n" "2. Isosceles Triangle\n" "3. Square / Rhombus\n" "4. Rectangle / Parallelogram\n" "5. Circle\n")
            sch = input("Enter shape choice [ 1 - 5 ]: ")
            print()
            match sch:
                case '1': # Equilateral Triangle
                    a = float(input("Enter Side Length [a] : "))
                    print()
                    print(f"Perimeter :  {3*a}\n")
                case '2': # Isosceles Triangle
                    a = float(input("Enter Equal Side's Length : "))
                    print()
                    b = float(input("Enter Non-Equal Side's Length : "))
                    print()
                    print(f"Area :  {2*a+b}\n") # Corrected to Perimeter
                case '3': # Square / Rhombus
                    a = float(input("Enter Length of Side [a] : "))
                    print()
                    print(f"Perimeter :  {4*a}\n")
                case '4': # Rectangle / Parallelogram
                    l = float(input("Enter Length of Rectangle / Parallelogram [l] : "))
                    print()
                    b = float(input("Enter Breadth of Rectangle / Parallelogram [l] : "))
                    print()
                    print(f"Perimeter :  {2*(l + b)}\n")
                case '5': # circle
                    r = float(input("Enter the Radius [r] : "))
                    print()
                    c = 2*mt.pi*r
                    print(f"Circumference :  {c}\n")
                case _:
                    print("Invalid Option! Exiting Perimeter Calculation ...\n")
        case '16': # Area [Various Shapes]
            print("Area Calculation [Various Shapes]\n"
                  "Select a shape : \n" "1. Equilateral Triangle\n" "2. Isosceles Triangle\n" "3. Square\n" "4. Rectangle / Parallelogram\n"
                  "5. Rhombus\n" "6. Circle\n" "7. Semi-circle\n")
            sch = input("Enter shape choice [ 1 - 7 ] : ")
            print()
            match sch:
                case '1': # Equilateral Triangle
                    a = float(input("Enter Side Length [a] : "))
                    print()
                    ar = (mt.sqrt(3) / 4) * mt.pow(a, 2)
                    print(f"Area :  {ar}\n")
                case '2': # Isosceles Triangle
                    a = float(input("Enter Equal Side's Length : "))
                    print()
                    b = float(input("Enter Non-Equal Side's Length : "))
                    print()
                    ar = mt.sqrt(4*mt.pow(a, 2) - mt.pow(b, 2)) / 4 # Corrected Area formula
                    print(f"Area :  {ar}\n")
                case '3': # Square
                    a = float(input("Enter Length of Side [a] : "))
                    print()
                    ar = mt.pow(a, 2)
                    print(f"Area :  {ar}\n")
                case '4': # Rectangle / Parallelogram
                    l = float(input("Enter Length of Rectangle / Parallelogram [l] : "))
                    print()
                    b = float(input("Enter Breadth of Rectangle / Parallelogram [l] : "))
                    print()
                    ar = l * b
                    print(f"Area :  {ar}\n")
                case '5': # Rhombus
                    d1 = float(input("Enter Diagonal 1 [d1] : "))
                    print()
                    d2 = float(input("Enter Diagonal 2 [d2] : "))
                    print()
                    area = 0.5 * d1 * d2
                    print(f"Area of Rhombus :  {area}\n")
                case '6': # circle
                    r = float(input("Enter the Radius [r] : "))
                    print()
                    area = mt.pi * mt.pow(r, 2)
                    print(f"Area :  {area}\n")
                case '7': # Semi-circle
                    r = float(input("Enter the Radius [r] : "))
                    print()
                    area = 0.5 * mt.pi * mt.pow(r, 2)
                    print(f"Area :  {area}\n")
                case _:
                    print("Invalid Option! Exiting Area Calculation ...\n")
        case '17': # Volume [Various Shapes]
            print("Volume Calculation [Various Shapes]\n"
                  "Select a shape : \n"  "1. Cube\n" "2. Cuboid\n" "3. Cylinder\n" "4. Cone\n" "5. Sphere\n")
            sch = input("Enter shape choice [ 1 - 5 ] : ")
            print()
            match sch:
                case '1': # Cube
                    a = float(input("Enter Length of Side [a] : "))
                    print()
                    vol = mt.pow(a, 3)
                    print(f"Volume :  {vol}\n")
                case '2': # Cuboid
                    l = float(input("Enter Length [l] : "))
                    print()
                    b = float(input("Enter Breadth [b] : "))
                    print()
                    h = float(input("Enter Height [h] : "))
                    print()
                    vol = l * b * h
                    print(f"Volume :  {vol}\n")
                case '3': # Cylinder
                    r = float(input("Enter the Radius [r] : "))
                    print()
                    h = float(input("Enter the Height [h] : "))
                    print()
                    vol = mt.pi * mt.pow(r, 2) * h
                    print(f"Volume :  {vol}\n")
                case '4': # Cone
                    r = float(input("Enter the Radius [r] : "))
                    print()
                    h = float(input("Enter the Height [h] : "))
                    print()
                    vol = (1/3) * mt.pi * mt.pow(r, 2) * h
                    print(f"Volume :  {vol}\n")
                case '5': # Sphere
                    r = float(input("Enter the Radius [r] : "))
                    print()
                    vol = (4/3) * mt.pi * mt.pow(r, 3)
                    print(f"Volume :  {vol}\n")
                case _:
                    print("Invalid Option! Exiting Volume Calculation ...\n")
        case '18' : # Surface Area [Various Shapes]
            print("Surface Area Calculation [Various Shapes]\n"
                  "Select a shape : \n" "1. Cube\n" "2. Cuboid\n" "3. Cylinder\n" "4. Cone\n" "5. Sphere\n")
            sch = input("Enter shape choice [ 1 - 5 ] : ")
            print()
            match sch:
                case '1': # Cube
                    a = float(input("Enter Length of Side [a] : "))
                    print()
                    sa = 6 * mt.pow(a, 2)
                    print(f"Surface Area :  {sa}\n")
                case '2': # Cuboid
                    l = float(input("Enter Length [l] : "))
                    print()
                    b = float(input("Enter Breadth [b] : "))
                    print()
                    h = float(input("Enter Height [h] : "))
                    print()
                    sa = 2 * (l * b + b * h + h * l)
                    print(f"Surface Area :  {sa}\n")
                case '3': # Cylinder
                    r = float(input("Enter the Radius [r] : "))
                    print()
                    h = float(input("Enter the Height [h] : "))
                    print()
                    sa = 2 * mt.pi * r * (r + h)
                    print(f"Surface Area :  {sa}\n")
                case '4': # Cone
                    r = float(input("Enter the Radius [r] : "))
                    print()
                    h = float(input("Enter the Height [h] : "))
                    print()
                    sa = mt.pi * r * (r + mt.sqrt(mt.pow(h, 2) + mt.pow(r, 2)))
                    print(f"Surface Area :  {sa}\n")
                case '5': # Sphere
                    r = float(input("Enter the Radius [r] : "))
                    print()
                    sa = 4 * mt.pi * mt.pow(r, 2)
                    print(f"Surface Area :  {sa}\n")
                case _:
                    print("Invalid Option! Exiting Surface Area Calculation ...\n")
        case '19' : # Curved Surface Area [Various Shapes]
            print("Curved Surface Area Calculation [Various Shapes]\n"
                  "Select a shape : \n" "1. Cylinder\n" "2. Cone\n" "3. Sphere\n")
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
                case '2': # Cone
                    r = float(input("Enter the Radius [r] : "))
                    print()
                    h = float(input("Enter the Height [h] : "))
                    print()
                    csa = mt.pi * r * mt.sqrt(mt.pow(h, 2) + mt.pow(r, 2))
                    print(f"Curved Surface Area :  {csa}\n")
                case '3': # Sphere
                    r = float(input("Enter the Radius [r] : "))
                    print()
                    csa = 2 * mt.pi * mt.pow(r, 2)
                    print(f"Curved Surface Area :  {csa}\n")
                case _:
                    print("Invalid Option! Exiting Curved Surface Area Calculation ...")
        case '20': # Diagonal Calculation [Various Shapes]
            print("Diagonal Calculation [Various Shapes]\n"
                  "Select a shape : \n" "1. Square\n" "2. Rectangle\n" "3. Cube\n" "4. Cuboid\n")
            sch = input("Enter shape choice [ 1 - 5 ] : ")
            print()
            match sch:
                case '1': # Square
                    a = float(input("Enter Length of Side [a] : "))
                    print()
                    d = mt.sqrt(2) * a
                    print(f"Diagonal :  {d}\n")
                case '2': # Rectangle
                    l = float(input("Enter Length [l] : "))
                    print()
                    b = float(input("Enter Breadth [b] : "))
                    print()
                    d = mt.sqrt(mt.pow(l, 2) + mt.pow(b, 2))
                    print(f"Diagonal :  {d}\n")
                case '3': # Cube
                    a = float(input("Enter Length of Side [a] : "))
                    print()
                    d = mt.sqrt(3) * a
                    print(f"Diagonal :  {d}\n")
                case '4': # Cuboid
                    l = float(input("Enter Length [l] : "))
                    print()
                    b = float(input("Enter Breadth [b] : "))
                    print()
                    h = float(input("Enter Height [h] : "))
                    print()
                    d = mt.sqrt(mt.pow(l, 2) + mt.pow(b, 2) + mt.pow(h, 2))
                    print(f"Diagonal :  {d}\n")
                case _:
                    print("Invalid Option! Exiting Diagonal Calculation ...")
        case '21': # Factorial Calculation
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
        case '22': # Exit Program
            exit(0)
        case _:  # Default Case
            print("Please enter a Valid Input! Restarting PyCalc ...\n") 
            continue
    next_calc = input("Do you Want to Perform Another Calculation? [y/n]: ") # Next_Calc Loop 
    print()
    if next_calc.lower() == "n" or next_calc.lower() == "no" : break
    else : print("Please enter a Valid Input! Restarting PyCalc ...\n")
    continue
