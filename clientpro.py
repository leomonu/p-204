
from glob import glob
import socket
from tkinter import *
from  threading import Thread
from PIL import ImageTk, Image

screen_width = None
screen_height = None

SERVER = None
PORT = None
IP_ADDRESS = None


canvas1 = None

playerName = None
nameEntry = None
nameWindow = None


def saveName():
    global SERVER
    global playerName
    global nameWindow
    global nameEntry

    playerName = nameEntry.get()
    nameEntry.delete(0,END)
    nameWindow.destroy()

    SERVER.send(playerName.encode())


#Teacher write code here for askPlayerName()
def askPlayerName():
    global playerName
    global nameEntry
    global nameWindow 
    global canvas1 
    global  screen_height
    global screen_width

    nameWindow = Tk()
    nameWindow.title("Tambola Game")
    nameWindow.attributes("-fullscreen",True)

    screen_width = nameWindow.winfo_screenwidth()
    screen_height=nameWindow.winfo_screenheight()

    bg=ImageTk.PhotoImage(file="./assets/download.jpg")

    canvas1 = Canvas(nameWindow,width=500,height=500)
    canvas1.pack(fill="both",expand=True)
    canvas1.create_image(850,700,image=bg,anchor="nw")
    canvas1.create_text(screen_width/2,screen_height/5,text="ENTER NAME",font={"Chalkboard SE",80},fill="blue")

    nameEntry=Entry(nameWindow,width=25,justify="center",font={"Chalkboard SE",90},bg="white")
    nameEntry.place(x=screen_width/2-100,y=screen_height/3)    

    button= Button(nameWindow,text="save",font={"Chalkboard SE",90},bg="yellow",command=saveName)
    button.place(x=screen_width/2-30,y=screen_height/2)

    nameWindow.resizable(True,True)


    nameWindow.mainloop()


def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    PORT  = 8000
    IP_ADDRESS = '127.0.0.1'

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))


    # Creating First Window
    askPlayerName()




setup()
