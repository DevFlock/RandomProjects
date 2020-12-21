# Core
import tkinter as tk
import codecs
import random
root = tk.Tk()
asciiTable = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

# Functions

def checkHex():
    data = inputBox.get()
    inputBox.delete(0, tk.END)
    status.place(x=235, y=150)

    if data == hexChar[1]:
        status["text"] = "Correct!"
        status["fg"] = "green"
    else:
        status.place(x=180, y=150)
        status["text"] = f"Inorrect! - Answer: {hexChar[1]}"
        status["fg"] = "red"

    newHex()

def newHex():
    global hexChar
    randomSelection = asciiTable[random.randint(0, len(asciiTable)-1)]
    hexChar = [codecs.encode(bytes(randomSelection, "ascii"), "hex").decode("utf-8"), randomSelection]

    description["text"] = f"Convert {hexChar[0]} into ascii!"
    
# Modules

title = tk.Label(root, text="Hex Quiz", fg="black", font=("Helvetica", 27))
title.place(x=200, y=25)

status = tk.Label(root, text="", fg="black", font=("Helvetica", 15))
status.place(x=235, y=150)

description = tk.Label(root, text="Convert 00 into ascii!", fg="black", font=("Helvetica", 20))
description.place(x=150, y=100)

inputBox = tk.Entry(root, text="Input answer here.")
inputBox.place(x=200, y=200)

confirmButton = tk.Button(root, text="Confirm.", command=checkHex)
confirmButton.place(x=230, y=250)

# Output

newHex()
root.geometry("550x400")
root.title("Hex Quiz")
root.mainloop()