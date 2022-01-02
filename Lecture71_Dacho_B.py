menuList=[]
priceList=[]

def showBill():
    totalPrice=0
    print('-----------My List------------')
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
        totalPrice += int(priceList[number])
    print("Total Price : ", totalPrice)

while True:
    menuName=input('Please enter your menu : ')
    if (menuName.lower()=="exit"):
        break
    else:
        menuPrice=input('Price : ')
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()