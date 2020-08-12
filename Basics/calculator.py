def calculator():
    print("------------------")
    print("=== Calculator ===")
    print("------------------")
    print("1 For Addition \n2 For Subtraction \n3 For Multiplication \n4 For Division \n5 For Modulation")

    operation=input("Enter your Choice :")

    if operation!="1" and operation!="2" and operation!="3" and operation!="4" and operation!="5":
        print("Invalid Choice")
        exit()

    num1=input("Enter your first number :")
    num2=input("Enter your second number :")

    convert1=int(num1)
    convert2=int(num2)

    if operation=="1":
        formula=convert1+convert2
        print ("The result is :"+str(formula))
    elif operation=="2":
        formula = convert1 - convert2
        print ("The result is :" + str(formula))
    elif operation=="3":
        formula = convert1 * convert2
        print ("The result is :" + str(formula))
    elif operation=="4":
        formula = convert1 / convert2
        print ("The result is :" + str(formula))
    elif operation=="5":
        formula = convert1 % convert2
        print ("The result is :" + str(formula))

calculator()