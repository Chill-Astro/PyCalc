import math as mt
import requests
UPDATE_VERSION_URL = "https://gist.githubusercontent.com/Chill-Astro/e8c32d9a2b30780e3b6fd2819a51b330/raw/PyC_V.txt"
CURRENT_VERSION = "1.3"
def check_for_updates() : # Entire Update Check Thingy
    try:
        response = requests.get(UPDATE_VERSION_URL, timeout=5) # Fetch version file, timeout after 5 seconds
        response.raise_for_status()   # Raise HTTPError for bad responses
        latest_version = response.text.strip() # Get version string from file and remove whitespace
        if latest_version > CURRENT_VERSION:
            print("--- UPDATE AVAILABLE! ---")
            print(f"🎉 A NEW version of PyCalc is Available! : {latest_version}")
            print(f"Currently using : {CURRENT_VERSION}")
            print("Please visit github.com/Chill-Astro/PyCalc to download the latest release!") # Provide URL for Updates
            print("-----------------------")
        elif latest_version == CURRENT_VERSION:
            print("🎉 PyCalc is up to date!")
        else:
            print("⚠️ This is a DEV. Build of PyCalc!\n") # For development scenarios
    except requests.exceptions.RequestException as e:
        print("--- UPDATE CHECK FAILED! ---")
        print("⚠️ Could not check for updates. Please check your internet connection.")
        print(f"Error: {e}")
        print("------------------------")
    except Exception as e: # Catching other potential errors, like if the content of the file is not proper
        print("--- UPDATE CHECK FAILED ---")
        print("⚠️ Error occurred while checking for updates.")
        print(f"Error: {e}")
        print("------------------------")
def perform_binary_operation(operator, operation_func):
    try:
        x = float(input("Enter first number : "))
        y = float(input("Enter second number : "))
        print()
        print(x, operator, y, "=", operation_func(x, y))
        print()
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        print()
print("PyCalc : A Simple and Lightweight Calculator. Made in Python!") # Pycalc Starts here!
print(f"Version : {CURRENT_VERSION}") # Print Version
print()
check_for_updates() # Perform update check at startup
print()
print("Select a Mathematical Operation : ")
print()
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponents (x^y)")
print("6. Square Root")
print("7. Cube Root")
print("8. Approximate / Rounding")
print("9. Heron's Formula")
print("10. Simple Interest")
print("11. Compound Interest")
print("12. Prime No. Check")
print("13. Triangle Check")
print("14. Right Triangle Check")
print("15. Perimiter [Various Shapes]")
print("16. Area [Varoius Shapes]")
print("17. Volume [Various Shapes]")
print("18. Surface Area [Various Shapes]")
print("29. Curved Surface Area [Various Shapes]")
print("20. Diagonal Calculation [Various Shapes]")
print("21. Factorial Calculator")
print("22. Exit PyCalc")
while True:
    print()
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
                y = float(input("Enter second number : "))
                print()
                if y == 0:
                    print("Div. by Zero Not Defined!")
                else:
                    print(x, "/", y, "=", (x / y))
                print()
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                print()
        case '5': # Exponents
            perform_binary_operation("^", mt.pow)        
        case '6': # Square Root
            x = float(input("Enter a number : "))
            print()
            print("Root x = " , mt.sqrt(x))
            print()
        case '7': # Cube Root
            x = float(input("Enter a number : "))
            print()
            print("C. Root x = " , mt.cbrt(x))
            print()
        case '8':  # Rounding
            x = float(input("Enter a number : "))
            print()
            print(round(x))
            print()
        case '9': # Heron's Formula
            print("NOTE: Some Calculations may print 0.0 depending on the values!")
            print()
            a = float(input("Enter the first side [a] : "))
            b = float(input("Enter the second side [b] : "))
            c = float(input("Enter third side [c] : "))
            print()
            if(a <= 0 or b <= 0 or c <= 0): # Check for positive sides
                print("Sides must be +ve.")
                print()
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
            r = float(input("Enter the Rate [ as a percentage, ex : 10 for 10% ] : "))
            t = float(input("Enter the Time [ Years ] : "))
            print()
            si = p * r * t / 100
            print("Simple Interest : ", si)
            print("Amount : ", (si + p))
            print()
        case '11': # Compound Interest
            print("Compound Interest Calculation")
            print()
            p = float(input("Enter the Principal : "))
            r = float(input("Enter the Rate [ as a percentage, ex : 10 for 10% ] : "))
            n = float(input("Enter the number of times interest is compounded per year : "))
            t = float(input("Enter the Time [ Years ] : "))
            print()
            a = p * mt.pow((1 + r / (100 * n)), n * t)
            ci = a - p
            print("Compound Interest : ", ci)
            print("Amount : ", a)
            print()
        case '12' : # Prime Number Check
            x = int(input("Enter a Number : "))
            print()
            if x > 1:
                for i in range(2, x):
                    if (x % i) == 0:
                        print(x, "is not a Prime Number")
                        break
                else:
                    print(x, "is a Prime Number")
            else:
                print(x, "is not a Prime Number")
            print()
        case '13': # Triangle Check
            a = float(input("Enter first side [a] : "))
            b = float(input("Enter second side [b] : "))
            c = float(input("Enter third side [c] : "))
            print()
            if(a <= 0 or b <= 0 or c <= 0): # Check for positive sides
                print("Sides must be +ve")
                print()
                continue # Changed from 'break' to 'continue'
            elif (a + b > c) and (a + c > b) and (b + c > a):
                print("Valid Triangle")
            else:
                print("Not a Valid Triangle")
            print()
        case '14': # Right Triangle Check
            a = float(input("Enter first side [a] : "))
            b = float(input("Enter second side [b] : "))
            c = float(input("Enter third side [c] : "))
            print()
            if(a <= 0 or b <= 0 or c <= 0): # Check for positive sides
                print("Sides must be +ve")
                print()
                continue
            elif(mt.pow(a,2) + mt.pow(b,2) == mt.pow(c,2)) or (mt.pow(a,2) + mt.pow(c,2) == mt.pow(b,2)) or (mt.pow(b,2) + mt.pow(c,2) == mt.pow(a,2)): # Check all combinations for right triangle
                print("Is a Right Triangle")
            else:
                print("Not a Right Triangle.")
            print()
        case '15': # Perimeter [Various Shapes]
            print("Perimeter Calculation [Various Shapes]")
            print()
            print("Select a shape : ")
            print()
            print("1. Equilateral Triangle")
            print("2. Isosceles Triangle")
            print("3. Square / Rhombus")
            print("4. Rectangle / Parallelogram")
            print("5. Circle")
            print()
            sch = input("Enter shape choice [ 1 - 5 ]: ")
            print()
            match sch:
                case '1': # Equilateral Triangle
                    a = float(input("Enter Side Length [a] : "))
                    print()
                    print("Perimeter : ", 3*a)
                    print()
                case '2': # Isosceles Triangle
                    a = float(input("Enter Equal Side's Length : "))
                    b = float(input("Enter Non-Equal Side's Length : "))
                    print()
                    print("Area : ", 2*a+b) # Corrected to Perimeter
                    print()
                case '3': # Square / Rhombus
                    a = float(input("Enter Length of Side [a] : "))
                    print()
                    print("Perimeter : ", 4*a)
                    print()
                case '4': # Rectangle / Parallelogram
                    l = float(input("Enter Length of Rectangle / Parallelogram [l] : "))
                    b = float(input("Enter Breadth of Rectangle / Parallelogram [l] : "))
                    print()
                    print("Perimeter : ", 2*(l + b))
                    print()
                case '5': # circle
                    r = float(input("Enter the Radius [r] : "))
                    print()
                    c = 2*mt.pi*r
                    print("Circumference : ", c)
                    print()
                case _:
                    print("Invalid Option! Exiting Perimeter Calculation ...")
            print()
        case '16': # Area [Various Shapes]
            print("Area Calculation [Various Shapes]")
            print()
            print("Select a shape : ")
            print()
            print("1. Equilateral Triangle")
            print("2. Isosceles Triangle")
            print("3. Square")
            print("4. Rectangle / Parallelogram")
            print("5. Rhombus")
            print("6. Circle")
            print("7. Semi-circle")
            print()
            sch = input("Enter shape choice [ 1 - 7 ] : ")
            print()
            match sch:
                case '1': # Equilateral Triangle
                    a = float(input("Enter Side Length [a] : "))
                    print()
                    ar = (mt.sqrt(3) / 4) * mt.pow(a, 2)
                    print("Area : ", ar)
                    print()
                case '2': # Isosceles Triangle
                    a = float(input("Enter Equal Side's Length : "))
                    b = float(input("Enter Non-Equal Side's Length : "))
                    print()
                    ar = mt.sqrt(4*mt.pow(a, 2) - mt.pow(b, 2)) / 4 # Corrected Area formula
                    print("Area : ", ar)
                    print()
                case '3': # Square
                    a = float(input("Enter Length of Side [a] : "))
                    print()
                    ar = mt.pow(a, 2)
                    print("Area : ", ar)
                    print()
                case '4': # Rectangle / Parallelogram
                    l = float(input("Enter Length of Rectangle / Parallelogram [l] : "))
                    b = float(input("Enter Breadth of Rectangle / Parallelogram [l] : "))
                    print()
                    ar = l * b
                    print("Area : ", ar)
                    print()
                case '5': # Rhombus
                    d1 = float(input("Enter Diagonal 1 [d1] : "))
                    d2 = float(input("Enter Diagonal 2 [d2] : "))
                    print()
                    area = 0.5 * d1 * d2
                    print("Area of Rhombus : ", area)
                    print()
                case '6': # circle
                    r = float(input("Enter the Radius [r] : "))
                    print()
                    area = mt.pi * mt.pow(r, 2)
                    print("Area : ", area)
                    print()
                case '7': # Semi-circle
                    r = float(input("Enter the Radius [r] : "))
                    print()
                    area = 0.5 * mt.pi * mt.pow(r, 2)
                    print("Area : ", area)
                    print()
                case _:
                    print("Invalid Option! Exiting Area Calculation ...")
            print()
        case '17': # Volume [Various Shapes]
            print("Volume Calculation [Various Shapes]")
            print()
            print("Select a shape : ")
            print()
            print("1. Cube")
            print("2. Cuboid")
            print("3. Cylinder")
            print("4. Cone")
            print("5. Sphere")
            print()
            sch = input("Enter shape choice [ 1 - 5 ] : ")
            print()
            match sch:
                case '1': # Cube
                    a = float(input("Enter Length of Side [a] : "))
                    print()
                    vol = mt.pow(a, 3)
                    print("Volume : ", vol)
                    print()
                case '2': # Cuboid
                    l = float(input("Enter Length [l] : "))
                    b = float(input("Enter Breadth [b] : "))
                    h = float(input("Enter Height [h] : "))
                    print()
                    vol = l * b * h
                    print("Volume : ", vol)
                    print()
                case '3': # Cylinder
                    r = float(input("Enter the Radius [r] : "))
                    h = float(input("Enter the Height [h] : "))
                    print()
                    vol = mt.pi * mt.pow(r, 2) * h
                    print("Volume : ", vol)
                    print()
                case '4': # Cone
                    r = float(input("Enter the Radius [r] : "))
                    h = float(input("Enter the Height [h] : "))
                    print()
                    vol = (1/3) * mt.pi * mt.pow(r, 2) * h
                    print("Volume : ", vol)
                    print()
                case '5': # Sphere
                    r = float(input("Enter the Radius [r] : "))
                    print()
                    vol = (4/3) * mt.pi * mt.pow(r, 3)
                    print("Volume : ", vol)
                    print()
                case _:
                    print("Invalid Option! Exiting Volume Calculation ...")
            print()
        case '18' : # Surface Area [Various Shapes]
            print("Surface Area Calculation [Various Shapes]")
            print()
            print("Select a shape : ")
            print()
            print("1. Cube")
            print("2. Cuboid")
            print("3. Cylinder")
            print("4. Cone")
            print("5. Sphere")
            print()
            sch = input("Enter shape choice [ 1 - 5 ] : ")
            print()
            match sch:
                case '1': # Cube
                    a = float(input("Enter Length of Side [a] : "))
                    print()
                    sa = 6 * mt.pow(a, 2)
                    print("Surface Area : ", sa)
                    print()
                case '2': # Cuboid
                    l = float(input("Enter Length [l] : "))
                    b = float(input("Enter Breadth [b] : "))
                    h = float(input("Enter Height [h] : "))
                    print()
                    sa = 2 * (l * b + b * h + h * l)
                    print("Surface Area : ", sa)
                    print()
                case '3': # Cylinder
                    r = float(input("Enter the Radius [r] : "))
                    h = float(input("Enter the Height [h] : "))
                    print()
                    sa = 2 * mt.pi * r * (r + h)
                    print("Surface Area : ", sa)
                    print()
                case '4': # Cone
                    r = float(input("Enter the Radius [r] : "))
                    h = float(input("Enter the Height [h] : "))
                    print()
                    sa = mt.pi * r * (r + mt.sqrt(mt.pow(h, 2) + mt.pow(r, 2)))
                    print("Surface Area : ", sa)
                    print()
                case '5': # Sphere
                    r = float(input("Enter the Radius [r] : "))
                    print()
                    sa = 4 * mt.pi * mt.pow(r, 2)
                    print("Surface Area : ", sa)
                    print()
                case _:
                    print("Invalid Option! Exiting Surface Area Calculation ...")
            print()
        case '19' : # Curved Surface Area [Various Shapes]
            print("Curved Surface Area Calculation [Various Shapes]")
            print()
            print("Select a shape : ")
            print()        
            print("1. Cylinder")
            print("2. Cone")
            print("3. Sphere")
            print()
            sch = input("Enter shape choice [ 1 - 3 ] : ")
            print()
            match sch:
                case '1': # Cylinder
                    r = float(input("Enter the Radius [r] : "))
                    h = float(input("Enter the Height [h] : "))
                    print()
                    csa = 2 * mt.pi * r * h
                    print("Curved Surface Area : ", csa)
                    print()
                case '2': # Cone
                    r = float(input("Enter the Radius [r] : "))
                    h = float(input("Enter the Height [h] : "))
                    print()
                    csa = mt.pi * r * mt.sqrt(mt.pow(h, 2) + mt.pow(r, 2))
                    print("Curved Surface Area : ", csa)
                    print()
                case '3': # Sphere
                    r = float(input("Enter the Radius [r] : "))
                    print()
                    csa = 2 * mt.pi * mt.pow(r, 2)
                    print("Curved Surface Area : ", csa)
                    print()
                case _:
                    print("Invalid Option! Exiting Curved Surface Area Calculation ...")
        case '20': # Diagonal Calculation [Various Shapes]
            print("Diagonal Calculation [Various Shapes]")
            print()
            print("Select a shape : ")
            print()
            print("1. Square")
            print("2. Rectangle")
            print("3. Cube")
            print("4. Cuboid")
            print()
            sch = input("Enter shape choice [ 1 - 5 ] : ")
            print()
            match sch:
                case '1': # Square
                    a = float(input("Enter Length of Side [a] : "))
                    print()
                    d = mt.sqrt(2) * a
                    print("Diagonal : ", d)
                    print()
                case '2': # Rectangle
                    l = float(input("Enter Length [l] : "))
                    b = float(input("Enter Breadth [b] : "))
                    print()
                    d = mt.sqrt(mt.pow(l, 2) + mt.pow(b, 2))
                    print("Diagonal : ", d)
                    print()
                case '3': # Cube
                    a = float(input("Enter Length of Side [a] : "))
                    print()
                    d = mt.sqrt(3) * a
                    print("Diagonal : ", d)
                    print()
                case '4': # Cuboid
                    l = float(input("Enter Length [l] : "))
                    b = float(input("Enter Breadth [b] : "))
                    h = float(input("Enter Height [h] : "))
                    print()
                    d = mt.sqrt(mt.pow(l, 2) + mt.pow(b, 2) + mt.pow(h, 2))
                    print("Diagonal : ", d)
                    print()
                case _:
                    print("Invalid Option! Exiting Diagonal Calculation ...")
            print()  
        case '21': # Factorial Calculation
            x = int(input("Enter a Number : "))
            print()
            if x < 0:
                print("Factorial Not Defined for Negative Numbers!")
            elif x == 0 or x == 1:
                print("Factorial of", x, "is 1")
            else:
                fact = 1
                for i in range(2, x + 1):
                    fact *= i
                print("Factorial of", x, "is", fact)
            print()          
        case '22    ': # Exit Program
            exit(0)
        case _:  # Default Case
            print("Please enter a Valid Input! Restarting PyCalc ...")
    next_calc = input("Do you Want to Perform Another Calculation? [y/n]: ") # Next_Calc Loop
    print()
    if next_calc.lower() == "n" or next_calc.lower() == "no" : break
    else : print("Please enter a Valid Input! Restarting PyCalc ...")
