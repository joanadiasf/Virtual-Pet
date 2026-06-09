import random
import tkinter as tk
from itertools import count

class ImageLabel(tk.Label):
    #image on window
    def load(self, im):
        self.im = im
        self.frames = []
        try:
            for i in count(1):
                self.frames.append(tk.PhotoImage(file=im, format=f'gif -index {i}'))
        except tk.TclError:
            pass
        self.loc = 0
        self.image = self.frames[0]
        self.after(0, self.next_frame)

    def next_frame(self):
        if self.frames:
            self.loc = (self.loc + 1) % len(self.frames)
            self.image = self.frames[self.loc]
            self.config(image=self.image)
            # delay = self.im.info.get('duration', 100)
            delay=100
            self.after(delay, self.next_frame)

#abri janela
window = tk.Tk()

#background
TRANSPARENT_COLOR = "magenta"
window.config(bg=TRANSPARENT_COLOR)
window.wm_attributes('-transparentcolor', TRANSPARENT_COLOR)

lbl =  ImageLabel(window, bg=TRANSPARENT_COLOR)
lbl.pack() 
lbl.load('C:\\Users\\al795\\Downloads\\cat.gif')   #carregar ficheiro

#window transparent
window.overrideredirect(True)


#loop
window.mainloop()
