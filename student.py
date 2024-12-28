from tkinter import*
from tkinter import ttk
#pip install pillow install kiya for images crop
from PIL import Image,ImageTk            #for input pillow lib.to us PIl
from tkinter import messagebox 
import mysql.connector
import cv2



class Student:
    def __init__(self,root):       #custructor call
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #================variables=========
        
        self.var_dep=StringVar()
        self.var_session=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_phone=StringVar()
        self.var_photo=StringVar()
        
        
        
        # first image
        img1=Image.open(r"C:\Users\RC\.spyder-py3\project\project_img\third_image.jpg")
        img1=img1.resize((510,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=510,height=130) 


        # second image
        img2=Image.open(r"C:\Users\RC\.spyder-py3\project\project_img\image.jpg")
        img2=img2.resize((510,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=510,height=130) 
        
      
        # third image
        img3=Image.open(r"C:\Users\RC\.spyder-py3\project\project_img\first_image.jpg")
        img3=img3.resize((540,130),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=540,height=130) 
        
        
        # bg image
        img4=Image.open(r"C:\Users\RC\.spyder-py3\project\project_img\bg.jpg")
        img4=img4.resize((1570,710),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1570,height=710) 
        
        #title
        title_lbl=Label(bg_img,text="STUDENT  MANAGENENT  SYSTEM",font=("time new roman",35,"bold"),bg="yellow",fg="green")
        title_lbl.place(x=300,y=5,width=900,height=50)
        
        main_frame=Frame(bg_img,bd=2,bg="sky blue")
        main_frame.place(x=15,y=62,width=1500,height=580)
        
        
        #left sideframe
        Left_frame=LabelFrame(main_frame,bd=4,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",16,"bold"))
        Left_frame.place(x=20,y=15,width=715,height=550)
      
            
        # current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",13,"bold"))
        current_course_frame.place(x=50,y=15,width=600,height=120)
        
        
        #department
        dep_label=Label(current_course_frame,text="Department :",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",10),state="readonly")
        dep_combo["values"]=("Select Department","BCA","B.tech","MCA","M.tech","Bio.tech","Geography","English","Economics")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
    
        #session
        session_label=Label(current_course_frame,text="Session :",font=("times new roman",12,"bold"),bg="white")
        session_label.grid(row=1,column=0,padx=10,sticky=W)
        
        session_combo=ttk.Combobox(current_course_frame,textvariable=self.var_session,font=("times new roman",10),state="readonly")
        session_combo["values"]=("Select Session","2021-24","2022-25","2023-26","2024-26")
        session_combo.current(0)
        session_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        
        #year
        year_label=Label(current_course_frame,text="Year :",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=2,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",10),state="readonly")
        year_combo["values"]=("Select Year","2021","2022","2023","2024","2025","2026")
        year_combo.current(0)
        year_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        
        #semester
        sem_label=Label(current_course_frame,text="Semester :",font=("times new roman",12,"bold"),bg="white")
        sem_label.grid(row=0,column=2,padx=10,sticky=W)
        
        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",10),state="readonly")
        sem_combo["values"]=("Select Semester","1","2","3","4","5","6")
        sem_combo.current(0)
        sem_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        
        # class student informtion
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student information",font=("times new roman",13,"bold"))
        class_student_frame.place(x=8,y=150,width=690,height=360)
        
        #student name
        studentName_lable=Label(class_student_frame,text="Student Name :",font=("times new roman",12,"bold"),bg="white")
        studentName_lable.grid(row=0,column=0,padx=5,pady=8,sticky=W)
     
        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=20,font=("times new roman",11)) 
        studentName_entry.grid(row=0,column=1,padx=5,sticky=W)
        
        
        #student id
        studentId_lable=Label(class_student_frame,text="StudentID :",font=("times new roman",12,"bold"),bg="white")
        studentId_lable.grid(row=0,column=2,padx=5,pady=8,sticky=W)
     
        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_id,width=20,font=("times new roman",11)) 
        studentID_entry.grid(row=0,column=3,padx=5,sticky=W)    
        
     
        #roll no
        roll_no_lable=Label(class_student_frame,text="Roll No.  :",font=("times new roman",12,"bold"),bg="white")
        roll_no_lable.grid(row=1,column=0,padx=5,sticky=W)
     
        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",11)) 
        roll_no_entry.grid(row=1,column=1,padx=5,pady=8,sticky=W) 
        
        
        #gender
        gender_label_lable=Label(class_student_frame,text="Gender :",font=("times new roman",12,"bold"),bg="white")
        gender_label_lable.grid(row=2,column=2,padx=5,sticky=W)
        
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",10),state="readonly")
        gender_combo["values"]=("Select gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=3,padx=5,pady=8,sticky=W)
        
     
        #DOB
        dob_label_lable=Label(class_student_frame,text="DOB  :",font=("times new roman",12,"bold"),bg="white")
        dob_label_lable.grid(row=2,column=0,padx=5,sticky=W)
     
        dob_label_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",11)) 
        dob_label_entry.grid(row=2,column=1,padx=5,pady=8,sticky=W) 
          
        
        #phone no
        phone_label_lable=Label(class_student_frame,text="Phone No.  :",font=("times new roman",12,"bold"),bg="white")
        phone_label_lable.grid(row=1,column=2,padx=5,sticky=W)
     
        phone_label_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",11)) 
        phone_label_entry.grid(row=1,column=3,padx=5,pady=8,sticky=W) 
     
        
        #radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=4,column=0,padx=9,pady=30,sticky=W)
        
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=4,column=1,padx=9,pady=30,sticky=W)
        
     
        #button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=7,y=200,width=671,height=37)
     
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=16,font=("time new roman",13,"bold"),bg="light blue",fg="black")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=16,font=("time new roman",13,"bold"),bg="light blue",fg="black")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=15,font=("time new roman",13,"bold"),bg="light blue",fg="black")
        delete_btn.grid(row=0,column=2)
     
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=16,font=("time new roman",13,"bold"),bg="light blue",fg="black")
        reset_btn.grid(row=0,column=3)
     
        btn_frame1=Frame(class_student_frame,bd=1,relief=RIDGE,bg="white")
        btn_frame1.place(x=7,y=255,width=671,height=47)
     
        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=33,font=("time new roman",13,"bold"),bg="light blue",fg="black")
        take_photo_btn.grid(row=0,column=0,padx=0,pady=10,sticky=W)
     
       # update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=32,font=("time new roman",13,"bold"),bg="light blue",fg="black")
       # update_photo_btn.grid(row=0,column=1,padx=0,pady=10,sticky=W)
        
        
       # =====================
       
        #right sideframe
        Right_frame=LabelFrame(main_frame,bd=4,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",16,"bold"))
        Right_frame.place(x=760,y=15,width=715,height=550) 
      
        #search system
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",13,"bold"))
        search_frame.place(x=50,y=15,width=600,height=75)
             
        search_lable=Label(search_frame,text="Search By :",font=("times new roman",12,"bold"),bg="red")
        search_lable.grid(row=0,column=0,padx=8,pady=5,sticky=W)
        self.var_searchTX=StringVar()
         
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_searchTX,font=("times new roman",10),state="readonly")
        search_combo["values"]=("Select","Roll No.")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        self.var_search=StringVar()
        search_entry=ttk.Entry(search_frame,textvariable=self.var_search,width=20,font=("times new roman",12,"bold")) 
        search_entry.grid(row=0,column=2,padx=5,pady=8,sticky=W) 
    
        search_btn=Button(search_frame,command=self.search_data,text="Search",width=10,font=("time new roman",8,"bold"),bg="light blue",fg="black")
        search_btn.grid(row=0,column=3,padx=2)
     
        showAll_btn=Button(search_frame,command=self.fetch_data,text="Show All",width=10,font=("time new roman",8,"bold"),bg="light blue",fg="black")
        showAll_btn.grid(row=0,column=4,padx=3)
    
    
        #table frame
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=8,y=150,width=690,height=360)
    
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","session","year","sem","id","name","roll","gender","dob","phone","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
    
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("session",text="Session")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll",text="Roll NO.")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("phone",text="Phone No.")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        
        self.student_table.column("dep",width=100)
        self.student_table.column("session",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=150)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("photo",width=150)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    
    #===========function Decration=============
    
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("error","All fields are required",parent=self.root)
        else: 
            try:
                mydb=mysql.connector.connect(host="127.0.0.1",user="root",database="face_recognizer",password="R@manand18")
                my_cursor=mydb.cursor()
                my_cursor.execute("insert into student value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                  self.var_dep.get(),
                                                                                                  self.var_session.get(),
                                                                                                  self.var_year.get(),
                                                                                                  self.var_sem.get(),
                                                                                                  self.var_id.get(),
                                                                                                  self.var_name.get(),
                                                                                                  self.var_roll.get(),
                                                                                                  self.var_gender.get(),
                                                                                                  self.var_dob.get(),
                                                                                                  self.var_phone.get(),
                                                                                                  self.var_radio1.get()  
                                                                                                    
                                                                                                ))
                mydb.commit()
                self.fetch_data()
                mydb.close()
                messagebox.showinfo("Success","Details has been successfully Save",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)   
            
    
    #===================fetch data==========
    
    def fetch_data(self):
        mydb=mysql.connector.connect(host="127.0.0.1",user="root",database="face_recognizer",password="R@manand18")
        my_cursor=mydb.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,value=i)
                mydb.commit()
        mydb.close()
    
    #===============get cursor==========
    
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0]),
        self.var_session.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_roll.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_phone.set(data[9]),
        self.var_radio1.set(data[10])
    
    
    #update button
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_session.get()=="Select Session" or self.var_year.get()=="Select Year" or self.var_sem.get()=="Select Semester" or self.var_id.get()=="" or self.var_name.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="Select gender" or self.var_dob.get()=="" or self.var_phone.get()=="":
            messagebox.showerror("Error","All fields are Required!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    mydb=mysql.connector.connect(host="127.0.0.1",user="root",database="face_recognizer",password="R@manand18")
                    my_cursor=mydb.cursor()
                    my_cursor.execute("update student set dep=%s,session=%s,year=%s,sem=%s,name=%s,roll=%s,gender=%s,dob=%s,phone=%s,photo=%s where id=%s",(
                    self.var_dep.get(),
                    self.var_session.get(),
                    self.var_year.get(),
                    self.var_sem.get(),                                                                                                                                        
                    self.var_name.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_phone.get(),
                    self.var_radio1.get(),
                    self.var_id.get()
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Details successfully update completed",parent=self.root)
                mydb.commit()
                self.fetch_data()
                mydb.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    
    #delete button
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student Id Must be Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete details","Do you want to delete this details?",parent=self.root)
                if delete>0:
                    mydb=mysql.connector.connect(host="127.0.0.1",user="root",database="face_recognizer",password="R@manand18")
                    my_cursor=mydb.cursor()
                    sql="delete from student where id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
    
                mydb.commit()
                self.fetch_data()
                mydb.close()
                messagebox.showinfo("Delete","Details are successfully deleted!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
    
    #reset button
    def reset_data (self):
        self.var_dep.set("Select Department")
        self.var_session.set("Select Session")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_roll.set("")
        self.var_gender.set("Select gender")
        self.var_dob.set("")
        self.var_phone.set("")
        self.var_radio1.set("")



# ===========================Search Data===================
    def search_data(self):
        if self.var_search.get()=="" or self.var_searchTX.get()=="Select":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                mydb = mysql.connector.connect(host="127.0.0.1",user="root",database="face_recognizer",password="R@manand18")
                my_cursor = mydb.cursor()
                sql = "SELECT dep,session,year,sem,id,name,roll,gender,dob,phone,photo FROM student where roll='" +str(self.var_search.get()) + "'" 
                my_cursor.execute(sql)
                # my_cursor.execute("select * from student where Roll_No= " +str(self.var_search.get())+" "+str(self.var_searchTX.get())+"")
                rows=my_cursor.fetchall()        
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        mydb.commit()
                mydb.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)    

#=====================This part is related to Opencv Camera part=======================
    
    #=====================Generate data set take a photo sample===============
    def generate_dataset(self):
          if self.var_dep.get()=="Select Department" or self.var_session.get()=="Select Session" or self.var_year.get()=="Select Year" or self.var_sem.get()=="Select Semester" or self.var_id.get()=="" or self.var_name.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="Select gender" or self.var_dob.get()=="" or self.var_phone.get()=="":
              messagebox.showerror("Error","All fields are required",parent=self.root)
          else:
              try:
                  mydb=mysql.connector.connect(host="127.0.0.1",user="root",database="face_recognizer",password="R@manand18")
                  my_cursor=mydb.cursor()
                  my_cursor.execute("select * from student")
                  myresult=my_cursor.fetchall()
                  id=0 
                  for x in myresult:
                      id+=1 
                  my_cursor.execute("update student set dep=%s,session=%s,year=%s,sem=%s,name=%s,roll=%s,phone=%s,gender=%s,dob=%s,photo=%s where id=%s",(
                        self.var_dep.get(),
                        self.var_session.get(),
                        self.var_year.get(),
                        self.var_sem.get(),                                                                                                                                        
                        self.var_name.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_phone.get(),
                        self.var_radio1.get(),
                        self.var_id.get()==id+1
                        ))
                  mydb.commit()
                  self.fetch_data()
                  self.reset_data()
                  mydb.close()
    
    
                  # =============== lord predefined data on front face take from open cv=================
                  
                  face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                  
                  def face_croped(img):
                      gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                      faces=face_classifier.detectMultiScale(gray,1.3,5)
                      #scaling factor =1.3
                      #minimum neighbour=5
                      for(x,y,w,h) in faces:
                          face_croped=img[y:y+h,x:x+w]
                          return face_croped
                       
                  cap=cv2.VideoCapture(0)
                  img_id=0 
                  while True:             
                        ret,my_frame=cap.read()
                        if face_croped(my_frame) is not None:
                           img_id+=1
                           face=cv2.resize(face_croped(my_frame),(450,450))
                           face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                           file_path="data_img/stdudent."+str(id)+"."+str(img_id)+".jpg"
                           cv2.imwrite(file_path,face)
                           cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)        
                           cv2.imshow("Capture Images",face)
                      
    #photosampe how much                       
                        if cv2.waitKey(1)==13 or int(img_id)==100:
                           break
                  cap.release()
                  cv2.destroyAllWindows()
                  messagebox.showinfo("Result","Generating data sets compled!!!!",parent=self.root)
              except Exception as es:
                  messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)    
              
    
    
    
    

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()