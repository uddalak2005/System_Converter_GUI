from tkinter import *
from tkinter import messagebox
import System_Converter
root=Tk()
root.title("System Converter")
root.geometry('800x600')
root.maxsize(800,600)
root.minsize(800,600)
root.iconbitmap("Icons/Icon.ico")
root.attributes('-alpha',0.92)
###############################################################################
Label(root,text='SYSTEM CONVERTER',font=('Envy Code R',50,'bold')).pack(pady=20)
binary=Label(root,text='Binary',font=('Envy Code R',20,'bold'))
binary.place(x=100,y=200)
deci=Label(root,text='Decimal',font=('Envy Code R',20,'bold'))
deci.place(x=100,y=250)
octal=Label(root,text='OCtal',font=('Envy Code R',20,'bold'))
octal.place(x=100,y=300)
hexa=Label(root,text='Hexadecimal',font=('Envy Code R',20,'bold'))
hexa.place(x=100,y=350)
####################################################################
####################################################################
####################################################################
bin_inp=Entry(root,font=('Envy Code R',18),justify=CENTER)
bin_inp.place(x=310,y=200)
def convert_binary():
    if bin_inp.get()=='':
        messagebox.showerror("Error!",'Please enter a value to be converted')
    else:
        a=str(System_Converter.binary_to_decimal(bin_inp.get()))
        deci_inp.insert(0,a)
        a=str(System_Converter.binary_to_octal(bin_inp.get()))
        octa_inp.insert(0,a)
        a= str(System_Converter.binary_to_hexa(bin_inp.get()))
        hexa_inp.insert(0,a)
con1 = PhotoImage(file='Icons/Untitled-1.png')
con1_btn = Button(root, image=con1, borderwidth=0, command=convert_binary)
con1_btn.place(x=600,y=195)
#####################################################################
deci_inp=Entry(root,font=('Envy Code R',18),justify=CENTER)
deci_inp.place(x=310,y=250)
def convert_decimal():
    if deci_inp.get()=='':
        messagebox.showerror("Error!",'Please enter a value to be converted')
    else:
        b = str(System_Converter.decimal_to_binary(deci_inp.get()))
        bin_inp.insert(0,b)
        b = str(System_Converter.decimal_to_octal(deci_inp.get()))
        octa_inp.insert(0,b)
        b = str(System_Converter.decimal_to_hexa(deci_inp.get()))
        hexa_inp.insert(0,b)
con2 = PhotoImage(file='Icons/Untitled-1.png')
con2_btn = Button(root, image=con2, borderwidth=0, command=convert_decimal)
con2_btn.place(x=600,y=245)
#############################################################################
octa_inp=Entry(root,font=('Envy Code R',18),justify=CENTER)
octa_inp.place(x=310,y=300)
def convert_octa():
    if octa_inp.get()=='':
        messagebox.showerror("Error!",'Please enter a value to be converted')
    else:
        c=str(System_Converter.octal_to_decimal(octa_inp.get()))
        deci_inp.insert(0,c)
        c=str(System_Converter.octal_to_binary(octa_inp.get()))
        bin_inp.insert(0,c)
        c = str(System_Converter.octal_to_hexa(octa_inp.get()))
        hexa_inp.insert(0,c)
con3 = PhotoImage(file='Icons/Untitled-1.png')
con3_btn = Button(root, image=con1, borderwidth=0, command=convert_octa)
con3_btn.place(x=600,y=295)
#############################################################################
hexa_inp=Entry(root,font=('Envy Code R',18),justify=CENTER)
hexa_inp.place(x=310,y=350)
def convert_hexa():
    if hexa_inp.get()=='':
        messagebox.showerror("Error!",'Please enter a value to be converted')
    else:
        d=str(System_Converter.hexa_to_decimal(hexa_inp.get()))
        deci_inp.insert(0,d)
        d=str(System_Converter.hexa_to_octal(hexa_inp.get()))
        octa_inp.insert(0,d)
        d = str(System_Converter.hexa_to_binary(hexa_inp.get()))
        bin_inp.insert(0,d)
con4 = PhotoImage(file='Icons/Untitled-1.png')
con4_btn = Button(root, image=con4, borderwidth=0, command=convert_hexa)
con4_btn.place(x=600,y=345)
#####################################################################
#####################################################################
def clear():
    bin_inp.delete(0,END)
    deci_inp.delete(0,END)
    octa_inp.delete(0,END)
    hexa_inp.delete(0,END)
########################################################################
def wrd(txt):
     text=""
     for i in range(0,len(txt)):
         text=text+txt[i]
         if i%100==0 and i!=0:
             text+="\n"
     return text
########################################################################
def exit_btn():
    if messagebox.askyesno('Exit','Do you really want to exit'):
        root.destroy()
#########################################################################
def learn():
    global btn,bg
    top=Toplevel()
    top.title('Learn about various systems and their interconversion')
    top.geometry('900x650')
    top.minsize(900,650)
    top.maxsize(900,650)
    top.attributes('-alpha',0.95)
    top.iconbitmap("Icons/Icon.ico")
    btn=PhotoImage(file="Icons/Learning.png")
    bg=PhotoImage(file="Icons/BG.png")
    my_canvas=Canvas(top,height=650,width=900)
    my_canvas.pack(fill='both',expand=True)
    my_canvas.create_image(0,0,image=bg,anchor="nw")
    my_canvas.create_image(450,2,image=btn,anchor="n")
    my_canvas.create_text(92,120,text='Binary Number-->',font=("Gabriola",16,'bold'))
    bin_txt = open('Binary_txt.txt', 'r', encoding='utf8')
    bin = bin_txt.read()
    my_canvas.create_text(50,180,text=wrd(bin),anchor='w',font=('Envy Code',12,'bold'))
    my_canvas.create_text(92, 250, text='Deimal Number-->', font=("Gabriola", 16, 'bold'))
    dec_txt = open('decimal.txt', 'r', encoding='utf8')
    dec = dec_txt.read()
    my_canvas.create_text(50, 310, text=wrd(dec), anchor='w', font=('Envy Code', 12, 'bold'))
    my_canvas.create_text(92, 380, text='Octal Number-->', font=("Gabriola", 16, 'bold'))
    oc_txt = open('Octal.txt', 'r', encoding='utf8')
    oc = oc_txt.read()
    my_canvas.create_text(50, 440, text=wrd(oc), anchor='w', font=('Envy Code', 12, 'bold'))
    my_canvas.create_text(120, 510, text='Hexadecimal Number-->', font=("Gabriola", 16, 'bold'))
    hex_txt = open('hexa.txt', 'r', encoding='utf8')
    hexi = hex_txt.read()
    my_canvas.create_text(50, 570, text=wrd(hexi), anchor='w', font=('Envy Code', 12,'bold'))

####################################################################################################
lrn=PhotoImage(file='Icons/Learn_Button.png')
lrn_btn=Button(root,image=lrn,borderwidth=0,command=learn)
lrn_btn.place(x=50,y=450)
cl=PhotoImage(file='Icons/Clear_button.png')
cl_btn=Button(root,image=cl,borderwidth=0,command=clear)
cl_btn.place(x=300,y=450)
exi=PhotoImage(file='Icons/Exit_button.png')
exi_btn=Button(root,image=exi,borderwidth=0,command=exit_btn)
exi_btn.place(x=550,y=450)
root.mainloop()