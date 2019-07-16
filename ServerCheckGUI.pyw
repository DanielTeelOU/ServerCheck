from tkinter import *
import tkinter.ttk as ttk
import os
import sys
import tkinter
import subprocess

#from ServerCheck import list_files, redirect_to_file1, redirect_to_file2, compare

#Window and header-----------------------------------------------------------------
window = tkinter.Tk()
window.iconbitmap(r'./TermIcon.ico')
window.geometry("373x410")
window.title("Server Check")
window.configure(background="black")
window.resizable(width=False, height=False)

#functions--------------------------------------------------------------------------
def list_files():
    for root, dirs, files in os.walk('C:\\'):
        level = root.replace('C://', '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

#compares the captured logs of the 2 systems
def compare():
    with open('output1.txt','r') as f:
        d=set(f.readlines())
    with open('output2.txt','r') as f:
        e=set(f.readlines())
    open('results.txt','w').close() #Create the file
    with open('results.txt','a') as f:
        for line in list(d-e):
            f.write(line)

#captures the system
def redirect_to_file1():
    original = sys.stdout
    sys.stdout = open('output1.txt', 'w')
    list_files()
    sys.stdout = original

#captures the system
def redirect_to_file2():
    original = sys.stdout
    sys.stdout = open('output2.txt', 'w')
    list_files()
    sys.stdout = original

#opens results text file
def openUp():
    os.system('results.txt')

#opens the log for the first log
def openfile1():
    os.system('output1.txt')

#opens the log for the second log
def openfile2():
    os.system('output2.txt')

#label--------------------------------------------------------------------------------------------------------------------------------------------------------
l = Label(window, text="ServerCheck", bg="gray20", fg="black", font="magneto 26", relief=GROOVE , width=14, height=2)
l.pack_propagate(0)
l.place(x=1, y=1)

#progress bar-------------------------------------------------------------------------------------------------------------------------------------------------
# s = ttk.Style()
# s.theme_use('classic')
# s.configure("red.Horizontal.TProgressbar", foreground='red', background='black', relief=GROOVE)
# pb_hD = ttk.Progressbar(window, style="red.Horizontal.TProgressbar", orient='horizontal', length=502, mode='indeterminate')
# pb_hD.pack(expand=True, side=tkinter.TOP)
# pb_hD.place(x=0, y=325)
# pb_hD.start(50)

#buttons-------------------------------------------------------------------------------------------------------------------------------------------------------
b1 = Button(window, text="$ Capture the log for system one", bg="black", fg="green2", font="consolas 11", relief=RAISED, width=45, height=2,command=redirect_to_file1) 
b1.place(x=1, y=99)
b2 = Button(window, text="$ View the log file for system one", bg="black", fg="green2", font="consolas 11", width=45, height=2, relief=RAISED,  command=openfile1)
b2.place(x=1, y=151)
b3 = Button(window, text="$ Capture the log for system two", bg="black", fg="green2", font="consolas 11", relief=RAISED, width=45, height=2, command=redirect_to_file2) 
b3.place(x=1, y=203)
b4 = Button(window, text="$ View the log file for system two", bg="black", fg="green2", font="consolas 11", width=45, height=2, relief=RAISED,  command=openfile2)
b4.place(x=1, y=255)
b5 = Button(window, text="$ Compare the logs of systems one and two", bg="black", fg="green2", font="consolas 11", relief=RAISED, width=45, height=2,  command=compare) 
b5.place(x=1, y=307)
b6 = Button(window, text="$ View the Results", bg="black", fg="green2", font="consolas 11", width=45, height=2, relief=RAISED,  command=openUp)
b6.place(x=1, y=359)

#run the program---------------------------------------------------------------------------------------------------------------------------------------------------
window.mainloop()