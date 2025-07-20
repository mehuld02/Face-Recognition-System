# main.py — Full Version with Buttons and GUI Images
from tkinter import *
from tkinter import ttk
import tkinter
import tkinter.messagebox
from PIL import Image, ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Top Images
        img = Image.open("images/Stanford.jpg")
        img=img.resize((500, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        img1 = Image.open("images/images2.jpeg")
        img1=img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        img2 = Image.open("images/cambridge.jpeg")
        img2=img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=130)

        # Background Image
        img3 = Image.open("images/background.jpg")
        img3=img3.resize((1300, 710), Image.LANCZOS)
        self.photobg = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photobg)
        bg_img.place(x=0, y=130, width=1300, height=710)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 30, "bold"), bg="white", fg="darkblue")
        title_lbl.place(x=0, y=0, width=1300, height=45)

        # Student Button
        img4 = Image.open("images/student.jpeg")
        img4=img4.resize((220, 220), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1 = Button(bg_img, image=self.photoimg4, command=self.student_details, cursor="hand2")
        b1.place(x=100, y=70, width=220, height=170)
        b1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=100, y=240, width=220, height=40)

        # Face Detector Button
        img5 = Image.open("images/face.jpg")
        img5=img5.resize((220, 220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1 = Button(bg_img, image=self.photoimg5, command=self.face_data, cursor="hand2")
        b1.place(x=400, y=70, width=220, height=170)
        b1_1 = Button(bg_img, text="Face Detector", command=self.face_data, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=400, y=240, width=220, height=40)

        # Attendance Button
        img6 = Image.open("images/attendance.jpg")
        img6=img6.resize((220, 220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b1 = Button(bg_img, image=self.photoimg6, command=self.attendance_data, cursor="hand2")
        b1.place(x=700, y=70, width=220, height=170)
        b1_1 = Button(bg_img, text="Attendance", command=self.attendance_data, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=700, y=240, width=220, height=40)

        # Help Desk Button
        img7 = Image.open("images/helpdesk.jpg")
        img7=img7.resize((220, 220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b1 = Button(bg_img, image=self.photoimg7, command=self.help_data, cursor="hand2")
        b1.place(x=1000, y=70, width=220, height=170)
        b1_1 = Button(bg_img, text="Help Desk", command=self.help_data, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1000, y=240, width=220, height=40)

        # Train Data Button
        img8 = Image.open("images/traindata.jpg")
        img8=img8.resize((220, 220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b1 = Button(bg_img, image=self.photoimg8, command=self.train_data, cursor="hand2")
        b1.place(x=100, y=300, width=220, height=170)
        b1_1 = Button(bg_img, text="Train Data", command=self.train_data, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=100, y=470, width=220, height=40)

        # Photos Folder Button
        img9 = Image.open("images/photo.jpg")
        img9=img9.resize((220, 220), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b1 = Button(bg_img, image=self.photoimg9, command=self.open_img, cursor="hand2")
        b1.place(x=400, y=300, width=220, height=170)
        b1_1 = Button(bg_img, text="Photos", command=self.open_img, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=400, y=470, width=220, height=40)

        # Developer Button
        img10 = Image.open("images/developer.jpg")
        img10=img10.resize((220, 220), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b1 = Button(bg_img, image=self.photoimg10, command=self.developer_data, cursor="hand2")
        b1.place(x=700, y=300, width=220, height=170)
        b1_1 = Button(bg_img, text="Developer", command=self.developer_data, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=700, y=470, width=220, height=40)

        # Exit Button
        img11 = Image.open("images/exit.png")
        img11=img11.resize((220, 220), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        b1 = Button(bg_img, image=self.photoimg11, command=self.iExit, cursor="hand2")
        b1.place(x=1000, y=300, width=220, height=170)
        b1_1 = Button(bg_img, text="Exit", command=self.iExit, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1000, y=470, width=220, height=40)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
