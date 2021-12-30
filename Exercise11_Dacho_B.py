bNumber=int(input("Please input the number : "))

for x in range(bNumber):
    print(" "*(bNumber-(x+1))+("*"*(x))+("*"*(x+1))+(" "*(bNumber-(x+1))))