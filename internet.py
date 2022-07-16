from tkinter import *
import speedtest

def speedcheck():
    sp=speedtest.Speedtest()
    sp.get_servers()
    
    down=str(round(sp.download()/(10**6),2))+ " Mbps"
    up=str(round(sp.upload()/(10**6),2))+ " Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

sp = Tk()
sp.title(" Internet Speed Test ")
sp.geometry("450x420")
sp.config(bg="navy")

lab = Label(sp,text="Internet Speed Test", font=("Times New Roman", 25,"bold"),bg="navy", fg="White")
lab.place(x=35, y=40, height=30, width=380)

lab = Label(sp,text="Download Speed", font=("Times New Roman", 17,"bold"),bg="lavender", fg="Red")
lab.place(x=125, y=130, height=30, width=200)

lab_down = Label(sp,text="00", font=("Times New Roman", 17,"bold"),bg="lavender", fg="Red")
lab_down.place(x=125, y=160, height=30, width=200)

lab = Label(sp,text="Upload Speed", font=("Times New Roman", 17,"bold"),bg="lavender", fg="Green")
lab.place(x=125, y=220, height=30, width=200)

lab_up = Label(sp,text="00", font=("Times New Roman", 17,"bold"),bg="lavender", fg="Green")
lab_up.place(x=125, y=250, height=30, width=200)

button = Button(sp,text="GO", font=("Times New Roman",14,"bold"),relief=RAISED,bg="tomato",command=speedcheck)
button.place(x=170, y=310, height=30, width=100)

sp.mainloop()