import tkinter as tk
from tkinter import *
from random import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import PhotoImage
from itertools import cycle

class AnimatedGIFBackground:
    def __init__(self, root, gif_path):
        self.root = root
        self.gif_path = gif_path
        self.frames = self.load_frames()
        self.frames_cycle = cycle(self.frames)
        self.current_frame = None
        self.bg_label = tk.Label(root)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.update_frame()

#    def _init_(self, root, gif_path):
#        self.root = root
#        self.gif_path = gif_path
#        self.frames = self.load_frames()
#        self.frames_cycle = cycle(self.frames)
#        self.current_frame = None
#        self.bg_label = tk.Label(root)
#        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
#        self.update_frame()

    def load_frames(self):
       # Load the GIF and iterate over its frames
       frames = []
       gif = PhotoImage(file=self.gif_path)
       try:
           for i in range(100):  # Assuming the GIF has fewer than 100 frames
               frame = PhotoImage(file=self.gif_path, format=f"gif -index {i}")
               frames.append(frame)
       except tk.TclError:
           pass  # Reached the end of the GIF frames
       return frames

    def update_frame(self):
       if self.frames:
           self.current_frame = next(self.frames_cycle)  # Get the next frame
           self.bg_label.config(image=self.current_frame)
           self.root.after(100, self.update_frame)  # Update the frame every 100 milliseconds


passGen= tk.Tk()
passGen.title('Password Generator')
passGen.geometry("500x300")


my_pass = chr(randint(33,126))

bg_image = PhotoImage(file="image/NvL.gif")
base = Frame(passGen)
base.pack(fill=BOTH, expand=TRUE)





animated_bg = AnimatedGIFBackground(base, "image/NvL.gif")




#bg_label = tk.Label(base, image=bg_image)
#bg_label.place(x=0, y=0, relwidth=1, relheight=1)



def new_rand():
    ret_entry.delete(0, END)

    #Getting password length

    pw_length= int(pass_entry.get())
    
    #Varable
    my_password =""

    for x in range(pw_length):
        my_password += chr(randint(33,126))

    ret_entry.insert(0, my_password)


def clips():
    passGen.clipboard_clear()

    passGen.clipboard_append(ret_entry.get())
    messagebox.showinfo("Copied to Clipboard", "The text has been copied to the clipboard.")


lf = LabelFrame(base, text= "Choose Number of Characters", fg="#15eb2e", width=270 , height=25, bg="black", font=20, borderwidth=2)
lf.pack(pady=30)


#entry box no of charcters
pass_entry= Entry(lf, font=("Helvetica", 24), bg="#15eb2e")
pass_entry.pack(pady=10, padx=20)
pass_entry.focus()

# returned password
ret_entry= Entry(base, text='', font=("helvetica", 24), bg="#15eb2e")
ret_entry.pack(pady=20)


#buttons
my_frame = Frame(base, bg="black")
my_frame.pack(pady=20)

my_button = Button(my_frame, text="Generate Password", command= new_rand, bg="black", fg="#15eb2e", )
my_button.grid(row=0,column=0, padx=10)

clip_button= Button(my_frame, text="Copy to Clipboard", command= clips, bg="black", fg="#15eb2e")
clip_button.grid(row=0,column=1,padx=10,)

passGen.mainloop()