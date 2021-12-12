usernameInput=input("Username : ")
passwordInput=input("Password : ")

if usernameInput=="admin"and passwordInput=="123qwe":
    print("----------Welcome to CP3 Shop-----------")
    smartphonePrice=1500
    smartwatchPrice=5600
    notebookPrice=12500
    chargerPrice=650
    print("1. Smart Phone (THB)",smartphonePrice)
    print("2. Smart Watch (THB)",smartwatchPrice)
    print("3. Notebook    (THB)",notebookPrice)
    print("4. Charger     (THB)",chargerPrice)
    print("----------------------------------------")
    userSelected=int(input("Please select to cart>> "))
    if userSelected==1:
        unit = int(input("Please input Q'ty (Unit) :"))

        print("You choose ",unit," Unit")
        print("Net Price (THB) :",smartphonePrice*unit)
        print("----------- Thank you very much -----------")
    elif userSelected==2:
        unit = int(input("Please input Q'ty (Unit) :"))

        print("You choose ",unit," Unit")
        print("Net Price (THB) :",smartwatchPrice*unit)
        print("----------- Thank you very much -----------")
    elif userSelected == 3:
        unit = int(input("Please input Q'ty (Unit) :"))

        print("You choose ", unit, " Unit")
        print("Net Price (THB) :", notebookPrice * unit)
        print("----------- Thank you very much -----------")
    elif userSelected == 4:
        unit = int(input("Please input Q'ty (Unit) :"))

        print("You choose ", unit, " Unit")
        print("Net Price (THB) :", chargerPrice * unit)
        print("----------- Thank you very much -----------")
    else:
        print("Sorry!!, Please select again")

else:
    print("Login Failed!!, Please try again")