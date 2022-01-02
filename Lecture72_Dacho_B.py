menuList=[]
def sumPrice():
    print('---------My List--------')
    total=0
    for i in range(len(menuList)):
        print(menuList[i][0],'=',menuList[i][1])
        total+=int(menuList[i][1])
    print('Net price :',total)

while True:
    menuName=input("Please enter your menu : ")
    if menuName.lower()=='exit':
        break
    else:
        menuPrice = input('Price : ')
        menuList.append([menuName,menuPrice])

sumPrice()
