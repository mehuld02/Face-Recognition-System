from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
from datetime import datetime
from dotenv import load_dotenv

load_dotenv() 

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #====variables=====
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        img = Image.open(r"images/facedetector.jpg")
        img = img.resize((800, 200), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=800, height=200)

        img1 = Image.open(r"images/detect.jpg")
        img1 = img1.resize((800, 200), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=800, y=0, width=800, height=200)

        img3 = Image.open("images/background.jpg")
        img3 = img3.resize((1300, 710), Image.LANCZOS)
        self.photobg = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photobg)
        bg_img.place(x=0, y=200, width=1300, height=710)

        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 30, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1300, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=55, width=1480, height=600)

        # Left Frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=640, height=370)

        img_left=Image.open(r"images/student.jpeg")
        img_left=img_left.resize((640,130),Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=640, height=130)

        left_inside_frame = Frame(left_frame, bd=2, bg="white",relief=RIDGE)
        left_inside_frame.place(x=0, y=135, width=630, height=210)

        Label(left_inside_frame, text="AttendanceID:", font=("times new roman", 12, "bold"), bg="white").grid(row=0, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_id, font=("times new roman", 12, "bold")).grid(row=0, column=1, padx=10, pady=5, sticky=W)

        Label(left_inside_frame, text="Roll:", font=("times new roman", 12, "bold"), bg="white").grid(row=0, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_roll, font=("times new roman", 12, "bold")).grid(row=0, column=3, padx=10, pady=5, sticky=W)

        Label(left_inside_frame, text="Name:", font=("times new roman", 12, "bold"), bg="white").grid(row=1, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_name, font=("times new roman", 12, "bold")).grid(row=1, column=1, padx=10, pady=5, sticky=W)

        Label(left_inside_frame, text="Department:", font=("times new roman", 12, "bold"), bg="white").grid(row=1, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_dep, font=("times new roman", 12, "bold")).grid(row=1, column=3, padx=10, pady=5, sticky=W)

        Label(left_inside_frame, text="Time:", font=("times new roman", 12, "bold"), bg="white").grid(row=2, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_time, font=("times new roman", 12, "bold")).grid(row=2, column=1, padx=10, pady=5, sticky=W)

        Label(left_inside_frame, text="Date:", font=("times new roman", 12, "bold"), bg="white").grid(row=2, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_date, font=("times new roman", 12, "bold")).grid(row=2, column=3, padx=10, pady=5, sticky=W)

        Label(left_inside_frame, text="Status:", font=("times new roman", 12, "bold"), bg="white").grid(row=3, column=0, padx=10, pady=5, sticky=W)
        self.atten_status = ttk.Combobox(left_inside_frame, textvariable=self.var_atten_attendance, font=("times new roman", 12, "bold"), state="readonly", width=18)
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3, column=1, pady=8)

        # Buttons
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=170, width=620, height=35)

        Button(btn_frame, text="Import CSV", command=self.importCsv, width=15, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=0)
        Button(btn_frame, text="Export CSV", command=self.exportCsv, width=15, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=1)
        Button(btn_frame, text="Update", width=15,command=self.update_data, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=2)
        Button(btn_frame, text="Reset", command=self.reset_data, width=15, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=3)

        # Right Frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=660, y=10, width=580, height=370)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=570, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,
            columns=("id", "roll", "name", "department", "time", "date", "attendance"),
            xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set
        )
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        for col, text in zip(("id", "roll", "name", "department", "time", "date", "attendance"),
                             ("Attendance ID", "Roll", "Name", "Department", "Time", "Date", "Attendance")):
            self.AttendanceReportTable.heading(col, text=text)
            self.AttendanceReportTable.column(col, width=100)

        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    def fetch_data(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV",
                                         filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                if i:  
                    mydata.append(i)
            self.fetch_data(mydata)

    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No Data Found To Export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV",
                                               defaultextension=".csv",
                                               filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                exp_write.writerow(["ID", "Roll", "Name", "Department", "Time", "Date", "Attendance"])
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Exported", f"Data exported to {os.path.basename(fln)} successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        row = content['values']
        if row:
            self.var_atten_id.set(row[0])
            self.var_atten_roll.set(row[1])
            self.var_atten_name.set(row[2])
            self.var_atten_dep.set(row[3])
            self.var_atten_time.set(row[4])
            self.var_atten_date.set(row[5])
            self.var_atten_attendance.set(row[6])

    def update_data(self):
        if self.var_dep.get()=="select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host=os.getenv("DB_HOST"),
                                                 user=os.getenv("DB_USER"),
                                                 password=os.getenv("DB_PASSWORD"),
                                                 database=os.getenv("DB_NAME"))
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Divison=%s,Roll=%s,Gender=%s,Email=%s,phone=%s,Dob=%s,Address=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                        self.var_std_id.get(),

                                                                                                                                                                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully updated completely",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
