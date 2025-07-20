from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import mysql.connector
import cv2
import os
import numpy as np
from dotenv import load_dotenv

load_dotenv() 

class Face_Recognition:
    # ========== Attendance ==========
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 30, "bold"), bg="white", fg="Red")
        title_lbl.place(x=0, y=0, width=1400, height=45)

        
        img_top = Image.open(r"images/facedetector.jpg")
        img_top=img_top.resize((700,600), Image.LANCZOS)
        self.photoimg_top= ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=600)

        img_bottom = Image.open(r"images/detect.jpg")
        img_bottom=img_bottom.resize((700,600), Image.LANCZOS)
        self.photoimg_bottom= ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55, width=650, height=600)

        b1_1 = Button(f_lbl, text="Face Recognition", cursor="hand2", font=("times new roman", 18, "bold"), bg="darkgreen", fg="white")
        b1_1.place(x=220, y=530, width=200, height=40)

        #====attendance===
    def mark_attendance(self,i,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list ) and (d not in name_list)) :
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")


    # ========== Face Recognition ==========
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbours, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbours)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0,255,0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn=mysql.connector.connect(host=os.getenv("DB_HOST"),
                                             user=os.getenv("DB_USER"),
                                             password=os.getenv("DB_PASSWORD"),
                                             database=os.getenv("DB_NAME"))
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(d)

                if confidence > 77:
                    cv2.putText(img, f"ID: {i}", (x, y-75), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img, f"Roll: {r}", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img, f"Name: {n}", (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img, f"Department: {d}", (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 3)
                    self.mark_attendance(i,r,n,d)

                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0,255,0), 3)
                    cv2.putText(img, f"Unknown Face:{d}", (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:  
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
