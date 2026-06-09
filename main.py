import random
import tkinter as tk
from itertools import count



class ImageLabel(tk.Label):
    #imagem na janela
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
lbl =  ImageLabel(window)
lbl.pack() 
lbl.load('C:\\Users\\al795\\Downloads\\cat.gif')   #carregar ficheiro

#loop
window.mainloop()

#janela abrir no canto TODO