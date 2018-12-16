from tkinter import *

def DoNothing():
    print("kk")

root = Tk()
#dropdown menu
dropdown = Menu(root)
root.config(menu = dropdown)

subMenu = Menu(dropdown)
dropdown.add_cascade(label = "File", menu = subMenu)
subMenu.add_command(label= "New project...", command = DoNothing)
subMenu.add_command(label= "New...", command = DoNothing)
subMenu.add_separator() 
subMenu.add_command(label= "Exit", command = quit)

editMenu = Menu(dropdown)
dropdown.add_cascade(label = "Edit", menu = editMenu)
editMenu.add_command(label = "Undo", command = DoNothing)
# The toolbar
toolbar = Frame(root, bg = "red")
insertbut = Button(toolbar, text = "insert image", command = DoNothing)
insertbut.pack(side = LEFT, padx = 2, pady = 2)
printButt = Button(toolbar, text = "Print", command = DoNothing)
printButt.pack(side = LEFT, padx = 2, pady = 2)
toolbar.pack(side = TOP, fill = X)
#Status bar
status = Label(root, text = "Preparing to do stuff", bd = 1, relief = SUNKEN, anchor = W)
status.pack(side = BOTTOM, fill = X )
root.mainloop()