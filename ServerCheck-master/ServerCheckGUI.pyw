from tkinter import *
import os
import sys
import tkinter
import subprocess
#from ServerCheck import list_files, redirect_to_file1, redirect_to_file2, compare
#Window and header-----------------------------------------------------------------
window = tkinter.Tk()
window.geometry("502x320")
window.title("ServerCheck GUI")
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

#label
l = Label(window, text="ServerCheck",bg="grey", fg="black", font="magneto 27", relief=GROOVE , width=19, height=2)
l.place(x=1, y=1)


#buttons-------------------------------------------------------------------------------------------------------------------------------------------------------
b1 = Button(window, text="Capture log for old system.", bg="black", fg="white", relief=RAISED, width=45, height=1,command=redirect_to_file1) 
b1.place(x=90, y=105)
b2 = Button(window, text="View the log file for the old system.", bg="black", fg="white", width=45, height=1, relief=RAISED,  command=openfile1)
b2.place(x=90, y=135)
b3 = Button(window, text="Capture log for new system.", bg="black", fg="white", relief=RAISED, width=45, height=1, command=redirect_to_file2) 
b3.place(x=90, y=170)
b4 = Button(window, text="View the log file for the new system.", bg="black", fg="white", width=45, height=1, relief=RAISED,  command=openfile2)
b4.place(x=90, y=205)
b5 = Button(window, text="Compare the logs of the old system with the new system.", bg="black", fg="white", relief=RAISED, width=45, height=1,  command=compare) 
b5.place(x=90, y=240)
b6 = Button(window, text="View the Results.", bg="black", fg="white", width=45, height=1, relief=RAISED,  command=openUp)
b6.place(x=90, y=275)



#run the program---------------------------------------------------------------------------------------------------------------------------------------------------
window.mainloop()