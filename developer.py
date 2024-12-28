from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk        
from tkinter import messagebox 
import mysql.connector
import cv2



class Developer:
    def __init__(self,root):       
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
     #title   
        title_lbl=Label(self.root,text="DEVELOPER",font=("time new roman",35,"bold"),bg="light blue",fg="blue")
        title_lbl.place(x=450,y=5,width=550,height=50)
        
       
        # bg image
        img_bg=Image.open(r"C:\Users\RC\.spyder-py3\project\project_img\b.jpg")
        img_bg=img_bg.resize((1570,730),Image.Resampling.LANCZOS)
        self.photoimg_bg=ImageTk.PhotoImage(img_bg)
        
        bg_img=Label(self.root,image=self.photoimg_bg)
        bg_img.place(x=0,y=55,width=1570,height=730)  
        
        #frame
        main_frame=LabelFrame(bg_img,bd=2,bg="white",relief=RIDGE,text="Developer information",font=("times new roman",13,"bold"))
        main_frame.place(x=315,y=20,width=800,height=520)
        
        
        # ramanand
        img_bg1=Image.open(r"C:\Users\RC\.spyder-py3\project - Copy\project_img\RC1.png")
        img_bg1=img_bg1.resize((180,190),Image.Resampling.LANCZOS)
        self.photoimg_bg1=ImageTk.PhotoImage(img_bg1)
        
        bg_img=Label(main_frame,image=self.photoimg_bg1)
        bg_img.place(x=310,y=10,width=180,height=190)  
        
        #info lable
        dev_label=Label(main_frame,text="Hello My name RC \n I am full stack Developer",font=("times new roman",12),bg="white")
        dev_label.place(x=320,y=200)
        
    
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()         