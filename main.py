
from tkinter import *
win=Tk()
cv=Canvas(win,width=800,height=500)
cv.pack()

print("\n\n2本の値線を引く　その交点を表示する \n")
print("値線1 y=al*x+b1 の　a1 と　b1を 入力")
a1 = float(input("  -5<a1<5 a1="))
b1 = float(input("  -3<b1<5 b1="))
print("値線　2 y=a2*x+b2 の　a2 と　b2 を　入力")
a2 = float(input("  -5<a2<5 a2="))
b2 = float(input("  -3<b2<5 b2="))

