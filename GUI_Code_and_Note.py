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

'''
Self-Notes: Here we arranged values in the form of 3 columns 
so we want some widget in center we should change the column value from 0 to 1
'''
# Create instance
win = tk.Tk()   

# Add a title       
win.title("Python GUI")

'''
We will create "monty" a child of main window frame "win"
and will replace every occurrence of win with monty and all the widget will be contained in "monty" 
'''
# We are creating a container frame to hold all other widgets
monty = ttk.LabelFrame(tab1, text=' Monty Python ')
monty.grid(column=0, row=0, padx=8, pady=4)

# Disable resizing the GUI
#win.resizable(0,0)   
# we can hard code this value (1,2) etc

# Modify adding a Label
aLabel = ttk.Label(monty, text="A Label")
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

ttk.Label(monty, text="Enter a name:").grid(column=0, row=0)

# Adding a Textbox Entry widget
name = tk.StringVar() # to take input from user
nameEntered = ttk.Entry(monty, width=12, textvariable=name) 
# testvariable is assigned to input variable
nameEntered.grid(column=0, row=1)


# Adding a Button 
action = ttk.Button(monty, text="Click Me!", command=clickMe)   
# command  for calling clickMe fumction
action.grid(column=2, row=1)
#action.configure(state='disabled')   
# Disable the Button Widget

'''
Adding a combobox to select from drop down
state is readonly so that user will not able to write in combo box
'''
ttk.Label(monty, text="Select a Number:").grid(column=1, row=0)
number = tk.StringVar()
numberchose = ttk.Combobox(monty, width = 12, textvariable=number, state = 'readonly')
numberchose['values'] = (1,2,3,4,100)
numberchose.grid(column =1, row = 1)
numberchose.current(0)

'''
'''
# Creating three checkbuttons


chVarDis = tk.IntVar()# this variable will be created for every check button as we can select multiple buttons
check1 = tk.Checkbutton(monty, text="Disabled", variable=chVarDis, state='disabled')
check1.select() 
# to select the checkbox
check1.grid(column=0, row=4, sticky=tk.W) 
# W show alignment to west grid i.e left side    
             

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(monty, text="UnChecked", variable=chVarUn) 
# variable is assigned to intvar()
check2.deselect() 
# to deselect the checkbox
check2.grid(column=1, row=4, sticky=tk.W)                   

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(monty, text="Enabled", variable=chVarEn)
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

rad1 = tk.Radiobutton(monty, text=COLOR1, variable=radVar, value=1, command=radCall)# from Command we called radCall method and value of radVar will be passed 
rad1.grid(column=0, row=5, sticky=tk.W, columnspan=3)   

rad2 = tk.Radiobutton(monty, text=COLOR2, variable=radVar, value=2, command=radCall)
rad2.grid(column=1, row=5, sticky=tk.W, columnspan=3)  

rad3 = tk.Radiobutton(monty, text=COLOR3, variable=radVar, value=3, command=radCall)
rad3.grid(column=2, row=5, sticky=tk.W, columnspan=3)

'''
'''
# Using a scrolled Text control    
scrolW  = 30  # These are the std values which we use but we can change them for experimental purpose
scrolH  =  3
scr = scrolledtext.ScrolledText(monty, width=scrolW, height=scrolH, wrap=tk.WORD)# wrap=tk.WORD to break lines by words 
																			   #if we use wrap = tk.char then will wrap around the word
#scr.grid(column=0, sticky='WE', columnspan=3)# sticky = WE is for west alignment 
scr.grid(column=0, columnspan=3)# so our scroll text will have 3 column of space initially

'''
Changing radio button using for loop
'''
# First, we change our Radiobutton global variables into a list.
colors = ["Blue", "Gold", "Red"]

# We have also changed the callback function to be zero-based, using the list instead of module-level global variables. 
# Radiobutton callback function
def radCall():
    radSel=radVar.get()
    if   radSel == 0: win.configure(background=colors[0])
    elif radSel == 1: win.configure(background=colors[1])
    elif radSel == 2: win.configure(background=colors[2])

radVar = tk.IntVar()

# Next we are selecting a non-existing index value for radVar.
radVar.set(99)    
'''# so that radio button with value 99 will be selected 
so that we don't have anything coded for value 99 no effect is displayed '''

# Now we are creating all three Radiobutton widgets within one loop.
for col in range(3): 
	'''# if we want to create 100 of these radio buttons we just have to change value from 3 to 100
    curRad = 'rad' + str(col) # what does it do?  It is just taking string rad and converting value of column to str() '''
	using type casting and then just storing it so 3 line above will reduced to 1 line 
    curRad = tk.Radiobutton(monty, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=6, sticky=tk.W)
'''
'''
# Create a container to hold labels

labelsFrame = ttk.LabelFrame(monty, text=' Labels in a Frame ')
labelsFrame.grid(column=0, row=7, padx=20, pady=40)


# Place labels into the container element
ttk.Label(labelsFrame, text="Label1").grid(column=0, row=0, sticky=tk.W)

# This will arrange the labels horizontally But
# we can arrange it vertically by changing the row value as row =0 row =1 etc
ttk.Label(labelsFrame, text="Label2").grid(column=1, row=0, sticky=tk.W)
ttk.Label(labelsFrame, text="Label3").grid(column=2, row=0, sticky=tk.W)

#To add padding after each child in label field
for child in labelsFrame.winfo_children(): 
    child.grid_configure(padx=8, pady=4)


'''
'''


nameEntered.focus()      # Place cursor into name Entry
#======================
# Start GUI
#======================
win.mainloop()