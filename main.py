from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk     #for input pillow lib.to us PIL
import tkinter
import os
from time import strftime
from datetime import datetime
from student import Student       #for access the file
from train import Train
from developer import Developer
from help import Help
from face_recognition import Face_Recognition
from attendance import Attendance



class Face_Recognition_System:
    def __init__(self,root):       #custructor call
        self.root=root
        self.root.geometry("1530x790+0+0")
       # self.root.configure(bg="light blue")
        self.root.title("Face Recognition System")
        
        # first image
        img1=Image.open(r"C:\Users\RC\.spyder-py3\project\project_img\first_image.jpg")
        img1=img1.resize((510,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=510,height=130) 
        
       #time clock 
        def time():
            string = strftime('%H:%M:%S %p')
            label.config(text=string)
            label.after(1000, time)
            
        label = Label(f_lbl, font=("ds-digital",15),background="black",foreground="cyan")
        label.place(x=30,y=87,width=128,height=37)
        time()


        # second image
        img2=Image.open(r"C:\Users\RC\.spyder-py3\project\project_img\second_image.jpg")
        img2=img2.resize((510,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=510,height=130) 
        
      
        # third image
        img3=Image.open(r"C:\Users\RC\.spyder-py3\project\project_img\third_image.jpg")
        img3=img3.resize((540,130),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=540,height=130) 
        
        
        # bg image
        img4=Image.open(r"C:\Users\RC\.spyder-py3\project\project_img\bg1.jpg")
        img4=img4.resize((1570,710),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1570,height=710) 
        
        
        title_lbl=Label(bg_img,text="FACE  RECOGNITION  ATTENDANCE  SYSTEM",font=("time new roman",35,"bold"),bg="yellow",fg="black")
        title_lbl.place(x=100,y=0,width=1330,height=60)
    
    
        #student button
        img5=Image.open(r"C:\Users\RC\.spyder-py3\project\project_img\Students Detail.jpg")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
    
        b1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("time new roman",15,"bold"),bg="dark blue",fg="white")
        b1.place(x=200,y=300,width=220,height=40)
        
        
        #Face Detector button
        img6=Image.open(r"C:\Users\RC\.spyder-py3\project\project_img\Face Detector.jpg")
        img6=img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)
    
        b1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("time new roman",15,"bold"),bg="dark blue",fg="white")
        b1.place(x=500,y=300,width=220,height=40)
        
        
        #Attendence button
        img7=Image.open(r"C:\Users\RC\.spyder-py3\project\project_img\Attendence.jpg")
        img7=img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)
    
        b1=Button(bg_img,text="Attendence",cursor="hand2",command=self.attendance_data,font=("time new roman",15,"bold"),bg="dark blue",fg="white")
        b1.place(x=800,y=300,width=220,height=40)
        
        
        
        #Help Desk button
        img8=Image.open(r"C:\Users\RC\.spyder-py3\project\project_img\Help Desk.jpg")
        img8=img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width=220,height=220)
    
        b1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("time new roman",15,"bold"),bg="dark blue",fg="white")
        b1.place(x=1100,y=300,width=220,height=40)
        
        
        
        #Train Data button
        img9=Image.open(r"C:\Users\RC\.spyder-py3\project\project_img\Train Data.jpg")
        img9=img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)
    
        b1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("time new roman",15,"bold"),bg="dark blue",fg="white")
        b1.place(x=200,y=580,width=220,height=40)
        
        
        
        #Photos button
        img10=Image.open(r"C:\Users\RC\.spyder-py3\project\project_img\Photos.jpg")
        img10=img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)
    
        b1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("time new roman",15,"bold"),bg="dark blue",fg="white")
        b1.place(x=500,y=580,width=220,height=40)
        
        
        
        #Developer button
        img11=Image.open(r"C:\Users\RC\.spyder-py3\project\project_img\Developer.jpg")
        img11=img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=380,width=220,height=220)
    
        b1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("time new roman",15,"bold"),bg="dark blue",fg="white")
        b1.place(x=800,y=580,width=220,height=40)
        
        
        
        #Exit button
        img12=Image.open(r"C:\Users\RC\.spyder-py3\project\project_img\Exit.jpg")
        img12=img12.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg12=ImageTk.PhotoImage(img12)
        
        b1=Button(bg_img,image=self.photoimg12,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=380,width=220,height=220)
    
        b1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("time new roman",15,"bold"),bg="dark blue",fg="white")
        b1.place(x=1100,y=580,width=220,height=40)
        
    def open_img(self):
        os.startfile("data_img")
        
        
    #exit function
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iExit >0:
           self.root.destroy()
        else:
            return
        
        
    #===================Function Buttons=====================
          
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
        
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
        
    
        
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
        
        
        
    
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
        
        
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)    
        
        
        
        
        
        

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop() 
    
