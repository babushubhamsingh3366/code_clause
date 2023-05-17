
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import time
import random
import difflib
from PIL import ImageTk,Image


class MainWindow:

    def __init__(self, root):
        self.text = ["Two roads diverged in a yellow wood",
                     "And be one traveler, long I stood",
                     "And looked down one as far as I could",
                     "To where it bent in the undergrowth",
                     "Then took the other, as just as fair",
                     "And having perhaps the better claim",
                     "Because it was grassy and wanted wear",
                     "Though as for that the passing there",
                     "Had worn them really about the same",
                     "And both that morning equally lay",
                     "In leaves no step had trodden black",
                     "Oh, I kept the first for another day",
                     "Yet knowing how way leads on to way",
                     "I doubted if I should ever come back"]



        self.speed = 0
        self.accuracy = 0
        self.time_start = 0
        self.time_end = 0


        root.title('speed Testing')
        root.geometry('1104x354+300+200')
        root.configure(bg='white')



        for row in range(5):
            root.grid_rowconfigure(row, weight=1)
        for col in range(3):
            root.grid_columnconfigure(col, weight=1)


        Label(root, text='', font=" family 12 bold  ", bg="#015a96", fg='white', height=18, width=55).place(x=546,
                                                                                                                y=3)

        Label(root, text='Typing speed Test', font=" family 12 bold  ", bg="red", fg='white',width=17,height=0).place(x=60, y=110)

        self.label_text = Label(
            root, text="Hello! welcome to typing speed", font="family 14  normal ",bg='#015a96',fg='white')
        self.label_text.place(x=670,y=40)

        self.user_text = Text(root,width=43,height=2,bg='#015a96',font=" family 13 bold ",fg='white')
        self.user_text.place(x=630,y=110)

        self.btn_start = Button(root, text="Start/Restart",font=" family 10 normal ",bg="grey",fg='black',width=12, command=self.start)
        self.btn_start.place(x=630,y=200)

        self.btn_stop = Button(root, text="Stop",font=" family 10 normal ",bg="grey",fg='black',width=12, command=self.stop)
        self.btn_stop.place(x=775,y=200)

        self.btn_newtext = Button(root, text="New Text",font=" family 10  normal ",bg="grey",fg='black',width=12, command=self.new_text)
        self.btn_newtext.place(x=916,y=200)

        self.label_speed = Label(
            root, text=f"Time: {self.speed} ", font=" family 13 bold", bg='#015a96', fg='white')
        self.label_speed.place(x=630,y=275)

        self.label_speed = Label(
            root, text=f"WPM: {self.speed} ",font=" family 13 bold",bg='#015a96',fg='white')
        self.label_speed.place(x=775,y=275)

        self.label_accuracy = Label(
            root, text=f" Accuracy:{self.speed} %",font=" family 13 bold",bg='#015a96',fg='white')
        self.label_accuracy.place(x=916,y=275)


    def start(self):
        self.time_start = time.time()

    def stop(self):
        self.time_end = time.time()
        words = self.label_text.cget("text").split(' ')
        self.speed = round(len(words)/((self.time_end - self.time_start)/60))
        self.label_speed.config(
            text=f"WPM: {self.speed} ")
        self.accuracy = round(difflib.SequenceMatcher(None, self.label_text.cget(
            "text"), self.user_text.get("1.0", 'end-1c')).ratio()*100)
        self.label_accuracy.config(
            text=f"Accuracy: {self.accuracy} %")

    def new_text(self):
        self.label_text.config(
            text=self.text[random.randint(0, len(self.text)-1)])
        self.user_text.delete('1.0', END)



def main():
    root = Tk()

    image1 = Image.open("C:\\Users\\HP\\Downloads\\woman-3190829_960_720.jpg")
    image1 = image1.resize((1100, 350))
    image1 = ImageTk.PhotoImage(image1)
    myLabel1 = Label(root, image=image1, bg='white')
    myLabel1.place(x=0, y=0)

    myapp = MainWindow(root)

    root.mainloop()



if __name__ == "__main__":
     main()






