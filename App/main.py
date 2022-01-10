import tkinter as tk

# Top level window
frame = tk.Tk()
frame.title("SUGGESTION")
frame.geometry('500x250')

# Function for getting Input
# from textbox and printing it
# at label widget
label_1 = tk.Label(frame, text="Suggestion: ", width=20, font=("bold", 15))
label_1.place(x=0, y=10)


def printInput():
    inp = input_txt.get(1.0, "end-1c")
    if inp:
        lbl.config(text="Provided Input: " + inp + "      [DATA SAVED]")
    else:
        lbl.config(text="Provided Input: " + "[Data Not Saved]")


# TextBox Creation
input_txt = tk.Text(frame, height=2, width=20)

input_txt.pack()

# Button Creation
printButton = tk.Button(frame, text="Click to Save", command=printInput, bg="black", fg="blue")
printButton.pack()

# Label Creation
lbl = tk.Label(frame, text="")
lbl.pack()
frame.mainloop()
