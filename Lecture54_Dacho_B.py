def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "dacho" and passwordInput == "123qwe":
        print(showMenu())
    else:
        print("Please try again !!")
        print(login())
def showMenu():
    print("------------My Shop-------------")
    print("1.Vat Calculator")
    print("2.Price Calculator")
    print(menuSelect())
def menuSelect():
    userSelect = int(input(">>"))
    if userSelect==1:
        price3=int(input("Please input Product Price : "))
        print("Product net price is :",vatCal(price3),"THB")
        print(showMenu())
    else:
        print(priceCal())
def vatCal(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result
def priceCal():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    netPrice = vatCal(price1 + price2)
    return netPrice
    print(netPrice())
print(login())