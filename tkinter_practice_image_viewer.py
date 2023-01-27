#This programs opens a .jpg or .png file on the canvas widget.
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

#window 
window = tk.Tk()
window.title('Image Viewer')
window.resizable()

#functions
def open_file():
    global display_image
    explore = filedialog.askopenfile(mode = 'rb', initialdir = '/', title = 'Select a file', filetypes = (('JPEG', '.jpg'), ('PNG', '*.png')))

    display_image = ImageTk.PhotoImage(Image.open(explore))

    img = canvas.create_image(0, 0, anchor = 'nw', image = display_image)
    
    bbox = canvas.bbox(img)
    width = bbox[2]
    height = bbox[3]

    canvas.configure(scrollregion = (0, 0, width, height))

#menu
menu = tk.Menu(window)
window.configure(menu = menu)

#sub-menu
file_menu = tk.Menu(window, tearoff = False)
file_menu.add_command(label = 'Open', command = open_file)
menu.add_cascade(label = 'File', menu = file_menu)

#widgets
canvas = tk.Canvas(window, background = 'gray')
canvas.pack(expand = True, fill = 'both')

#events
canvas.bind('<MouseWheel>', lambda event: canvas.yview_scroll(-int(event.delta / 60), 'units'))
canvas.bind('<ButtonPress-1>', lambda event: canvas.scan_mark(event.x, event.y))
canvas.bind('<B1-Motion>', lambda event: canvas.scan_dragto(event.x, event.y, gain = 1))

#run
window.mainloop()