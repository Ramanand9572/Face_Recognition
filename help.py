from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk        
from tkinter import messagebox 
import mysql.connector
import cv2




class Help:
    def __init__(self,root):       
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.configure(bg="light blue")
        self.root.title("Face Recognition System")
     #title   
        title_lb2=Label(self.root,text="HELP  DESK",font=("time new roman",40,"bold"),bg="light blue",fg="blue")
        title_lb2.place(x=505,y=5,width=550,height=50)
  
  
       
        # bg image
        img_bg2=Image.open(r"C:\Users\RC\.spyder-py3\project\project_img\c.jpg")
        img_bg2=img_bg2.resize((1570,730),Image.Resampling.LANCZOS)
        self.photoimg_bg2=ImageTk.PhotoImage(img_bg2)
        
        bg_img=Label(self.root,image=self.photoimg_bg2)
        bg_img.place(x=0,y=55,width=1550,height=730)  
        
        dev_label=Label(bg_img,text="Hi, how can we help you?", font=("times new roman",25,"bold"),bg="white")
        dev_label.place(x=600,y=100)
        
        dev_label2=Label(bg_img,text=("* Managing Students details \n * Removing data                    \n * Deleting students data         \n * Update data                         \n * How to train image             \n * How to add data                 "), font=("times new roman",15),bg="white")
        dev_label2.place(x=640,y=160)
    
        dev_label=Label(bg_img,text="Please visit this email :- helpattendance@gmai.com // anand@gmail.com \n contact no. :- 9006222782,  9639547719                                                     ", font=("times new roman",13),bg="white")
        dev_label.place(x=630,y=400)



if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()         