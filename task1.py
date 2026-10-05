def calc():
    while True:
        print("\n1.+\n2.-\n3.*\n4./\n5.km to miles\n6.C to F\n7.exit")
        ch=input("Choose: ")

        if ch=="7":
            break

        if ch in ["1","2","3","4"]:
            while True:
                try:
                    a=float(input("Enter first number: "))
                    b=float(input("Enter second number: "))
                    if ch=="4" and b==0:
                        print("Cannot divide by zero")
                        continue
                    break
                except ValueError:
                    print("Enter valid numbers")

            if ch=="1":
                print("Result:",a+b)
            elif ch=="2":
                print("Result:",a-b)
            elif ch=="3":
                print("Result:",a*b)
            else:
                print("Result:",a/b)

        elif ch=="5":
            while True:
                try:
                    km=float(input("Enter km: "))
                    print("Miles:",km*0.621371)
                    break
                except ValueError:
                    print("Enter a valid number")

        elif ch=="6":
            while True:
                try:
                    c=float(input("Enter Celsius: "))
                    print("Fahrenheit:",(c*9/5)+32)
                    break
                except ValueError:
                    print("Enter a valid number")

        else:
            print("Invalid choice")

calc()
