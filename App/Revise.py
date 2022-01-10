from tkinter import *


class WindowDesign:

    def __init__(self):
        root = Tk()
        root.title("Bag Weight")
        # root.geometry("500x700")
        root.wm_iconbitmap('favicon.ico')

        image = PhotoImage(file="Weight Program.png")
        imagelabel = Label(root, image=image)
        imagelabel.pack()

        weightentrylabel = Label(root, text="Enter Weight!")
        weightentrylabel.pack()

        self.string = StringVar()
        weightentry = Entry(root, textvariable=self.string)
        weightentry.pack()

        menutext = Label(root, text="What coin are you using?")
        # menutext.pack(side=LEFT)
        menutext.pack()

        values = ['1p', '2p', '5p', '10p', '20p', '50p', '£1', '£2', 'Exit']

        button1 = Button(root, text="1p", command=self.btn1)
        # button1.pack(side=LEFT)
        button1.pack()

        # --------------------------------------------------
        self.result = StringVar()
        resultlabel = Label(root, textvariable=self.result)
        resultlabel.pack()
        # --------------------------------------------------

        root.mainloop()

    # -------------------------------------
    def btn1(self):
        p1 = 3.56
        p1should = 356
        if not self.string.get(): return

        value = int(self.string.get())
        if value > p1should:
            weightdif = value - p1should
            coins = weightdif / p1

        elif value < p1should:
            weightdif = p1should - value
            coins = weightdif / p1

        self.result.set(coins)
    # -----------------------------------


WindowDesign()
