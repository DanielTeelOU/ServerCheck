s = ttk.Style()
s.theme_use('classic')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='black', relief=GROOVE)
pb_hD = ttk.Progressbar(window, style="red.Horizontal.TProgressbar", orient='horizontal', length=502, mode='indeterminate')
pb_hD.pack(expand=True, side=tkinter.TOP)
pb_hD.place(x=0, y=325)
pb_hD.start(50)