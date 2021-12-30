def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result
print("Your net price is ",vatCalculate(int(input("Please your price : "))),"THB")