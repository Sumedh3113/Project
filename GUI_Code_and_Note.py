'''
July 5,  2018
@author: Sumedh Deshpande
'''
#======================
# imports
#======================
import tkinter as tk 
# as tk is alias so that we can use it in code
from tkinter import ttk  # for adding widget we use
from tkinter import scrolledtext # for adding a scrollbar and text box


# Create instance
win = tk.Tk()   

# Add a title       
win.title("Python GUI")

# Disable resizing the GUI
#win.resizable(0,0)   
# we can hard code this value (1,2) etc

# Modify adding a Label
aLabel = ttk.Label(win, text="A Label")
aLabel.grid(column=0, row=0)

#Modified Button Click Function
def clickMe():
	'''
	action is a variable created below for configuring button
	text Hello will be displayed initially on button
	'''
    action.configure(text='Hello ' + name.get()+' '+number.get())
	# .get() to access the value entered by user

# Changing our Label
# .grid() value changes as 00,01,10,11

ttk.Label(win, text="Enter a name:").grid(column=0, row=0)

# Adding a Textbox Entry widget
name = tk.StringVar() # to take input from user
nameEntered = ttk.Entry(win, width=12, textvariable=name) 
# testvariable is assigned to input variable
nameEntered.grid(column=0, row=1)


# Adding a Button 
action = ttk.Button(win, text="Click Me!", command=clickMe)   
# command  for calling clickMe fumction
action.grid(column=2, row=1)
#action.configure(state='disabled')   
# Disable the Button Widget

'''
Adding a combobox to select from drop down
state is readonly so that user will not able to write in combo box
'''
ttk.Label(win, text="Select a Number:").grid(column=1, row=0)
number = tk.StringVar()
numberchose = ttk.Combobox(win, width = 12, textvariable=number, state = 'readonly')
numberchose['values'] = (1,2,3,4,100)
numberchose.grid(column =1, row = 1)
numberchose.current(0)

# Creating three checkbuttons


chVarDis = tk.IntVar()# this variable will be created for every check button as we can select multiple buttons
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state='disabled')
check1.select() 
# to select the checkbox
check1.grid(column=0, row=4, sticky=tk.W) 
# W show alignment to west grid i.e left side                 

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text="UnChecked", variable=chVarUn) 
# variable is assigned to intvar()
check2.deselect() 
# to deselect the checkbox
check2.grid(column=1, row=4, sticky=tk.W)                   

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)                     
'''
'''
# Radiobutton Globals
COLOR1 = "Blue" # These are the symbolic names of colors
COLOR2 = "Gold"
COLOR3 = "Red"

# Radiobutton Callback
def radCall():
    radSel=radVar.get()
	'''
	# we create only one variable here as only one button will be selected at a time and 
	will fetch value from radVar if 1 will change color to Blue
	'''
    if   radSel == 1: win.configure(background=COLOR1)
    elif radSel == 2: win.configure(background=COLOR2)
    elif radSel == 3: win.configure(background=COLOR3)

# create three Radiobuttons using one variable
radVar = tk.IntVar()

rad1 = tk.Radiobutton(win, text=COLOR1, variable=radVar, value=1, command=radCall)# from Command we called radCall method and value of radVar will be passed 
rad1.grid(column=0, row=5, sticky=tk.W, columnspan=3)   

rad2 = tk.Radiobutton(win, text=COLOR2, variable=radVar, value=2, command=radCall)
rad2.grid(column=1, row=5, sticky=tk.W, columnspan=3)  

rad3 = tk.Radiobutton(win, text=COLOR3, variable=radVar, value=3, command=radCall)
rad3.grid(column=2, row=5, sticky=tk.W, columnspan=3)
'''
'''
# Using a scrolled Text control    
scrolW  = 30  # These are the std values which we use but we can change them for experimental purpose
scrolH  =  3
scr = scrolledtext.ScrolledText(win, width=scrolW, height=scrolH, wrap=tk.WORD)# wrap=tk.WORD to break lines by words 
																			   #if we use wrap = tk.char then will wrap around the word
scr.grid(column=0, columnspan=3)# so our scroll text will have 3 column of space initially


nameEntered.focus()      # Place cursor into name Entry
#======================
# Start GUI
#======================
win.mainloop()