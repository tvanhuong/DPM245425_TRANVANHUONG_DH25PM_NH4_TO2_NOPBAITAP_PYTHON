from tkinter import *
from tkinter import Menu
window = Tk()
window.title('Lap trinh Tkinter')

menu = Menu(window)
new_item =Menu(menu)
new_item.add_command(label='new')
new_item.add_separator()
new_item.add_command(label='edit')
menu.add_cascade(label='file',menu=new_item)
window.config(menu=menu)

window.mainloop()