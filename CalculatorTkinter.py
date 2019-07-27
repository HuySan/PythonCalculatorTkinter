from tkinter import*
from tkinter import messagebox
from tkinter import ttk

my_window = Tk()
my_window.title('Yo')

#Buttons
btn = [
	'7','8','9','+','=',
	'4','5','6','-','',
	'1','2','3','*','',
	'0','.','/','C',''
]

roW = 1
columN =0
#Iterating over the array and making the buttons, structuring
for i in btn:
	ttk.Button(my_window,text = i,command = lambda x=i:calcLogic(x)).grid(row = roW,column = columN)
	columN+=1
	if columN > 4:
		columN = 0
		roW+=1

#The main logic of the calculator
def calcLogic(button):
	if button == "=":
		try:
			result = eval(valueEntry.get())
			valueEntry.insert(END,'=' + str(result))
		except:
			messagebox.showerror("Error!","Input is not correct!!!!!!!!!")
#Delete
	elif button == "C":
		valueEntry.delete(0,END)
	else:
		if "=" in valueEntry.get():
			valueEntry.delete(0,END)
		valueEntry.insert(END,button)

#data entry window
valueEntry = Entry(my_window,width = 33)
valueEntry.grid(row = 0,column = 0,columnspan = 5)

my_window.mainloop()