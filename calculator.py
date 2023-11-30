from tkinter import *
window=Tk()
window.title("normal calculator")
window.geometry("570x670+100+200")
window.resizable(False,False)
window.configure(bg="#17161b")
equation = ""

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation !="":
        try:
            result= eval(equation)
        except:
            result="error"
            equation=""
    label_result.config(text=result)

def show(value):
    global equation
    # Check if the last character in the equation is a mathematical symbol
    if equation and equation[-1] in '+-*/%':
        # If the new value is also a mathematical symbol, ignore it
        if value in '+-*/%':
            return
    equation += value
    label_result.config(text=equation)



label_result= Label(window,width=25,height=3,text="",font=("aerial",30), highlightbackground="grey", highlightthickness=10)
label_result.pack()
Button(window,width=5,height=1,text="C",font=("aerial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda: clear()).place(x=10,y=170)
Button(window,width=5,height=1,text="/",font=("aerial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("/")).place(x=150,y=170)
Button(window,width=5,height=1,text="%",font=("aerial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("%")).place(x=290,y=170)
Button(window,width=5,height=1,text="*",font=("aerial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("*")).place(x=430,y=170)

Button(window,width=5,height=1,text="7",font=("aerial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("7")).place(x=10,y=270)
Button(window,width=5,height=1,text="8",font=("aerial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("8")).place(x=150,y=270)
Button(window,width=5,height=1,text="9",font=("aerial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("9")).place(x=290,y=270)
Button(window,width=5,height=1,text="-",font=("aerial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("-")).place(x=430,y=270)

Button(window,width=5,height=1,text="4",font=("aerial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("4")).place(x=10,y=370)
Button(window,width=5,height=1,text="5",font=("aerial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("5")).place(x=150,y=370)
Button(window,width=5,height=1,text="6",font=("aerial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("6")).place(x=290,y=370)
Button(window,width=5,height=1,text="+",font=("aerial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("+")).place(x=430,y=370)

Button(window,width=5,height=1,text="1",font=("aerial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("1")).place(x=10,y=470)
Button(window,width=5,height=1,text="2",font=("aerial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("2")).place(x=150,y=470)
Button(window,width=5,height=1,text="3",font=("aerial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("3")).place(x=290,y=470)
Button(window,width=11,height=1,text="0",font=("aerial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("0")).place(x=10,y=570)

Button(window,width=5,height=1,text=".",font=("aerial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show(".")).place(x=290,y=570)
Button(window,width=5,height=3,text="=",font=("aerial",30,"bold"),bd=1,fg="#fff",bg="#fe9037",command=lambda: calculate()).place(x=430,y=470)






window.mainloop()