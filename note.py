import tkinter as tk

def add():
    global tl
    a=l.get()
    tl.append(a)
    j=tl.index(a)+1
    lb.insert(j,a)
    with open('task.txt','a') as f:
        f.write(a+'\n')
def dele():
    global tl
    t=lb.curselection()
    for i in t:
        tl.pop(i)
        with open('task.txt','w') as f:
            for j in tl:
                f.write(j+'\n')
        lb.delete(i)
    
tl=[]
try:
    with open('task.txt','r') as f:
        tl=f.read().split()
except:
    with open('task.txt','a') as f:
        pass

root=tk.Tk()
root.geometry("300x500")
root.title("Notes")
root.resizable(False,False)
root.config(bg="#fff0f3",bd=5)

tk.Label(root,text='To do List',height=2,width=100,font=('Times New Roman',18,'bold'),bg='#ffde21',fg='blue',bd=3).pack(pady=2)

im=tk.PhotoImage(file="note.png")
im=im.subsample(8,9)
tk.Label(root,image=im,height=35,width=30,bd=2).place(x=20,y=7)

im1=tk.PhotoImage(file="ink.png")
im1=im1.subsample(2,4)
tk.Label(root,image=im1,height=62,bd=2,bg="#fff0f3").place(x=48,y=70)

l=tk.StringVar()
e=tk.Entry(root,textvariable=l,width=150,font=('ariel',15),bd=3).place(x=0,y=170)

b=tk.Button(root,text='ADD',command=lambda:add(),font=('arial',11),bg='light blue').place(x=255,y=170)

lb=tk.Listbox(root,font=('ariel',11),width=40,height=25,bg='#00b4d8',cursor='hand2',selectbackground='#6ac5fe',bd=2)
lb.pack(padx=5,pady=(155,70))

for i in tl:
    j=tl.index(i)+1
    lb.insert(j,i)
    

im2=tk.PhotoImage(file="delete.png")
im2=im2.subsample(10,10)
b2=tk.Button(root,image=im2,height=43,width=45,bg='white',command=lambda:dele()).place(x=130,y=440)

root.mainloop()
