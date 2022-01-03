from tkinter import *
import math
def leftClickButton(event):
    x = float(textBoxWeight.get()) / math.pow(((float(textBoxHeight.get()) / 100)), 2)
    print(x)
    if x>30:
        labelCalculate.configure(text='อ้านมาก')
    elif x>=25:
        labelCalculate.configure(text='อ้าน')
    elif x>=23:
        labelCalculate.configure(text='น้ำหนักเกิน')
    elif x>=18.6:
        labelCalculate.configure(text='น้ำหนักปกติ เหมาะสม')
    elif x<18.6:
        labelCalculate.configure(text='ผอมเกินไป')
    else:
        print(x)
mainWindow=Tk()
labelHeight=Label(mainWindow,text="ส่วนสูง (cm)",font=("tahoma",12))
labelHeight.grid(row=0,column=0)
textBoxHeight=Entry(mainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeight=Label(mainWindow,text="น้ำหนัก (Kg)",font=("tahoma",12))
labelWeight.grid(row=1,column=0)
textBoxWeight=Entry(mainWindow)
textBoxWeight.grid(row=1,column=1)

calculateButton=Button(mainWindow,text="คำนวณ",font=("Tahoma",12))
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2,column=0)
labelCalculate=Label(mainWindow,text='ผลลัพธ์',font=('tahoma',12))
labelCalculate.grid(row=2,column=1)
mainWindow.mainloop()