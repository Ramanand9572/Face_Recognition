import re
from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime



class Face_Recognition:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        
        
        
        #title section
        title_lb1 = Label(self.root,text="Welcome to Face Recognition Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1530,height=50)

        
        # first image  
        img=Image.open(r"C:\Users\RC\.spyder-py3\project\project_img\1.jpg")
        img=img.resize((650,700),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=55,width=650,height=700)

        # second image 
        bg1=Image.open(r"C:\Users\RC\.spyder-py3\project\project_img\2.jpg")
        bg1=bg1.resize((900,700),Image.Resampling.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=650,y=55,width=900,height=700)



        # Training button 1
        img6=Image.open(r"C:\Users\RC\.spyder-py3\project\project_img\click.png")
        img6=img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_recog)
        b1.place(x=360,y=620,width=185,height=45)

      
       # std_b1_1 = Button(b1,command=self.face_recog,text="Face Detector",cursor="hand2",font=("tahoma",15,"bold"),bg="cyan",fg="navyblue")
       # std_b1_1.place(x=3,y=2,width=175,height=38)
        
        
        
        
        
    #=====================Attendance===================

    def mark_attendance(self,i,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])

            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")


    #================face recognition==================
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])

                confidence=int((100*(1-predict/300)))

                mydb=mysql.connector.connect(host="127.0.0.1",user="root",database="face_recognizer",password="R@manand18")
                my_cursor=mydb.cursor()
                
                                
                my_cursor.execute("select id from student where id="+str(id))
                i=my_cursor.fetchone()
               # i="+".join(i)
                
                
                my_cursor.execute("select roll from student where id="+str(id))
                r=my_cursor.fetchone()
               # r="+".join(r)


                my_cursor.execute("select name from student where id="+str(id))
                n=my_cursor.fetchone()
               # n="+".join(n)
                
              
                my_cursor.execute("select dep from student where id="+str(id))
                d=my_cursor.fetchone()
               # d="+".join(d)
                 


                if confidence > 77:
                    cv2.putText(img,f"Student ID:- 01 ",(x,y-105),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Roll No:- 11 ",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Name:- Ramanand ",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Department:- BCA ",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2) 
                    
                   # cv2.putText(img,f"Student ID:- {i} ",(x,y-105),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                   # cv2.putText(img,f"Roll No:- {r} ",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                   # cv2.putText(img,f"Name:- {n} ",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                   # cv2.putText(img,f"Department:- {d} ",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),2)    

                coord=[x,y,w,y]
            
            return coord    


        #==========
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        videoCap=cv2.VideoCapture(0)

        while True:
            ret,img=videoCap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Face Detector",img)

            if cv2.waitKey(1)==13:
                break
        videoCap.release()
        cv2.destroyAllWindows()




if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()