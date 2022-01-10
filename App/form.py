from tkinter import *
from os import system


def speak(Audio):
    system(f"say {Audio}")


# Creating object 'root' of Tk()
root = Tk()

# Providing Geometry to the form
root.geometry("500x600")
root.configure(background='white')
# w = OptionMenu(root, "Sunday", "Monday", "Tuesday",
#                "Wednesday", "Thursday", "Friday", "Saturday")

# Providing title to the form
root.title('Registration form')

# this creates 'Label' widget for Registration Form and uses place() method.
label = Label(root, text=" Registration form ", width=20, font=("bold", 20))
label_0 = Label(root, text="('*' portions are Compulsory) ", width=20, font=("italic", 10))
label.config(font=('', 20, ' underline italic'))
label_0.config(fg='grey', font=('', 10, "italic"))

# place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
label.place(x=120, y=40)
label_0.place(x=180, y=70)

# this creates 'Label' widget for Fullname and uses place() method.
label_1 = Label(root, text="Full Name*", width=20, font=("bold", 10))
label_1.place(x=80, y=110)

# this will accept the input string text from the user.
entry_1 = Entry(root)
entry_1.place(x=240, y=110)

# this creates 'Label' widget for Fullname and uses place() method.
label_2 = Label(root, text="Age*", width=20, font=("bold", 10))
label_2.place(x=80, y=160)

# this will accept the input string text from the user.
entry_2 = Entry(root)
entry_2.place(x=240, y=160)

# # this creates 'Label' widget for Email and uses place() method.
# label_3 = Label(root, text="Email", width=20, font=("bold", 10))
# label_3.place(x=68, y=180)

# entry_3 = Entry(root)
# entry_3.place(x=240, y=180)

# this creates 'Label' widget for Gender and uses place() method.
label_4 = Label(root, text="Gender*", width=20, font=("bold", 10))
label_4.place(x=70, y=210)

# the variable 'var' mentioned here holds Integer Value, by default 0
var = IntVar()

# this creates 'Radio button' widget and uses place() method
Radiobutton(root, text="Male", padx=5, variable=var, value=1).place(x=240, y=210)
Radiobutton(root, text="Female", padx=5, variable=var, value=2).place(x=300, y=210)

# this creates 'Label' widget for country and uses place() method.
label_5 = Label(root, text="Subjects", width=20, font=("bold", 10))
label_5.place(x=70, y=260)

# this creates list of countries available in the dropdown.
list_of_Sub = ['Python', 'java', 'R', 'C++', 'Kotlin']

# the variable 'str' mentioned here holds String Value, by default ""
Str = StringVar()
droplist = OptionMenu(root, Str, *list_of_Sub)
droplist.config(width=15)
Str.set('Select your Subject')
droplist.place(x=240, y=260)

# this creates 'Label' widget for Language and uses place() method.
label_6 = Label(root, text="Feedback", width=20, font=('bold', 10))
label_6.place(x=75, y=310)

# the variable 'var' mentioned here holds Integer Value, by default 0
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
# this creates Checkbutton widget and uses place() method.
Checkbutton(root, text="😞", variable=var1).place(x=230, y=310)

# this creates Checkbutton widget and uses place() method.
Checkbutton(root, text="😟", variable=var2).place(x=290, y=310)

# this creates Checkbutton widget and uses place() method.
Checkbutton(root, text="😊", variable=var3).place(x=350, y=310)

Checkbutton(root, text="😃", variable=var4).place(x=410, y=310)

# this creates 'Label' widget for country and uses place() method.
label_7 = Label(root, text="Code*", width=20, font=('bold', 10))
label_7.place(x=75, y=360)

# this will accept the input string text from the user.
entry_3 = Entry(root, show='*')
entry_3.place(x=230, y=360)


# this creates button for submitting the details provides by the user
def submitInput():
    inp = entry_1.get()
    inp2 = entry_2.get()
    pass_code = entry_3.get()
    if pass_code == '1234' and inp2 and inp:
        lbl.config(text="Access Successful!!\n DATA SAVED", fg='light green')
        speak("Access Successful! DATA SAVED")
    elif not inp and not inp2:
        lbl.config(text=f"Please fill the Compulsory sections!!", fg='red')
        speak("Please fill the Compulsory sections!!")
    elif pass_code != '1234':
        lbl.config(text='Access Denied Wrong Code!', fg='red')
        speak('Access Denied Wrong Code!')
    else:
        lbl.config(text="Access Denied [Data Not Saved]", fg='red')
        speak("Access Denied [Data Not Saved]")


# Button(root, text='ENTER', width=20, command="Data Saved", bg="black", fg='blue').place(x=180, y=380)
# Button Creation
SubmitButton = Button(root, text='ENTER', width=20, command=submitInput, fg='blue').place(x=150, y=410)
# printButton.pack()

# this will run the mainloop.
lbl = Label(root, text="")
lbl.pack(side='bottom', pady=20)
root.mainloop()
