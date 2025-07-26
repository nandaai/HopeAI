class MultipleFunctions:
    def Subfields():
        print( "Sub-fields in AI are:\nMachine Learning \nNeural Networks \nVision \nNatural Language Processing")

    def OddEven():
            n = int(input("Enter a number: "))
            if n%2 == 0:
                print( f"{n} is Even Number")
            else:
                print(f"{n} is Odd Number")

    def Eligible():
            Gen = input("Your Gender: ")
            Age = int(input("Your Age: "))
            if Gen == "Female":
                if Age < 18:
                    print("Not Eligible")
                else:
                    print("Eligible")
            else:
                if Age < 21:
                    print("Not Eligible")
                else:
                    print("Eligible")

    def percentage():
            i = 1
            total = 0
            for i in range(5):
                sub = "Subject" + str(i)
                sub = int(input(sub+ "="))
                total = total + sub
            per = total/5
            print("Total : ", total)
            print("Percentage :",per)

    def triangle():
            h = int(input("Height:"))
            b = int(input("Breadth:"))
            print("Area formula:(Height*Breadth)/2")
            print("Area of Triange: ", h*b/2)
            h1 = int(input("Height1:"))
            h2 = int(input("Height2:"))
            b1 = int(input("Breadth:"))
            print("Perimeter formula:Height1+Height2+Breadth")
            print("Permiter of Triangle: ", h1+h2+b1)

