import tkinter as tk
from tkinter import ttk

class Window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky=tk.S+tk.N+tk.E+tk.W)
        self.createWidgets()
    def createWidgets(self):
        top=self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        top.geometry("300x200")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.window = ttk.Frame(self, borderwidth=1, cursor='arrow')
        self.window.grid(row=0,column=0)
        self.label = ttk.Label(self.window, text='Installing...', font=('Calibri', 20, 'italic'))
        self.label.config(background='blue', foreground='cyan')
        self.label.grid(row=0,column=0,sticky=tk.N+tk.W, columnspan=2)
        self.select = ttk.OptionMenu(self, tk.StringVar(), "Select", "Option 1", "Option 2", "Option 3")
        self.select.grid(row=1, column=0, columnspan=2, sticky=tk.N+tk.W+tk.E)
        self.quit = ttk.Button(self, text='Quit', command=self.quit)
        self.quit.grid(row=2, column=1, sticky=tk.S+tk.E+tk.W)
        self.start = ttk.Button(self, text='Start')
        self.start.grid(row=2,column=0,sticky=tk.S+tk.E+tk.W)
        
app = Window()
app.master.title('Window')
app.mainloop()