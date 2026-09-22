import tkinter as tk
#create main window
root=tk.Tk()
root.title("simple calculator")
root.geometry("300x400")
#create text box
entry=tk.Entry(root,width=20,font=("Arial",18),justify="right")
entry.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
#function to insert value
def click(value):
    entry.insert(tk.END,value)
#function to calculate
def Calculate():
    try:
        result=eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(0,result)
    except:
        entry.delete(0,tk.END)
        entry.insert(0,"error")
#function to clear text box
def clear():
    entry.delete(0,tk.END)
#calculator buttons
buttons=[
    ("7",1,0),("8",1,1),("9",1,2),("/",1,3),
    ("4",2,0),("5",2,1),("6",2,2),("*",2,3),
    ("1",3,0),("2",3,1),("3",3,2),("-",3,3),
    ("0",4,0),(".",4,1),("+",4,2)
    ]
for text,row,column in buttons:
        tk.Button(
            root,
            text=text,
            width=5,
            height=2,
            font=("Arial",14),
            command=lambda value=text:click(value)
           ).grid(row=row,column=column,padx=5,pady=5)
#equal button
tk.Button(
    root,
    text="=",
    width=5,
    height=2,
    font=("Arial",14),
    command=Calculate
).grid(row=4,column=3,padx=5,pady=5)

#Clear button
tk.Button(
    root,
    text="CLEAR",
    width=23,
    height=2,
    font=("Arial",14),
    command=clear
).grid(row=5,column=0,columnspan=4,padx=5,pady=10)

#start GUI
root.mainloop()

