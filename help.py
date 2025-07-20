from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x700+0+0")
        self.root.title("Help Desk")

        # ==== Background Image ====
        self.bg_img = Image.open("images/background.jpg")
        self.bg_img = self.bg_img.resize((1300, 700), Image.LANCZOS)
        self.photo_bg = ImageTk.PhotoImage(self.bg_img)

        bg_label = Label(self.root, image=self.photo_bg)
        bg_label.place(x=0, y=0, width=1300, height=700)

        # ==== Title ====
        title_lbl = Label(self.root, text="HELP & SUPPORT", font=("times new roman", 30, "bold"), bg="#000000", fg="white")
        title_lbl.place(x=0, y=0, width=1300, height=60)

        # ==== Tabs ====
        style = ttk.Style()
        style.configure('TNotebook.Tab', font=('Arial', 14, 'bold'))

        tab_control = ttk.Notebook(self.root)
        self.contact_tab = Frame(tab_control, bg="white")
        self.usage_tab = Frame(tab_control, bg="white")
        self.faq_tab = Frame(tab_control, bg="white")
        self.about_tab = Frame(tab_control, bg="white")

        tab_control.add(self.contact_tab, text="Contact")
        tab_control.add(self.usage_tab, text="Usage")
        tab_control.add(self.faq_tab, text="FAQs")
        tab_control.add(self.about_tab, text="About")
        tab_control.place(x=170, y=100, width=900, height=500)

        # ==== Contact Tab ====
        Label(self.contact_tab, text="📧 Email: support@example.com", font=("Arial", 18), bg="white", fg="blue").pack(pady=20)
        Label(self.contact_tab, text="📞 Phone: +91-XXXXXXXXXX", font=("Arial", 18), bg="white", fg="blue").pack(pady=10)

        Button(self.contact_tab, text="📂 Visit GitHub", font=("Arial", 16, "bold"),
               bg="green", fg="white", width=20, height=2,
               command=lambda: webbrowser.open("https://github.com/your-repo")).pack(pady=30)

        # ==== Usage Tab ====
        Label(self.usage_tab, text="📘 How to Use the Application", font=("Arial", 20, "bold"), bg="white").pack(pady=20)
        usage_text = """
1. Register a new student by filling the form.
2. Capture the photo sample using webcam.
3. Train the face recognition model from the dataset.
4. Use the face recognition feature to mark attendance.
5. View and export attendance data.
        """
        Label(self.usage_tab, text=usage_text, justify=LEFT, font=("Arial", 16), bg="white").pack(padx=40)

        # ==== FAQ Tab ====
        Label(self.faq_tab, text="❓ Frequently Asked Questions", font=("Arial", 20, "bold"), bg="white").pack(pady=20)
        faq_text = """
Q1. What is this application for?
Ans: It’s a Face Recognition-based Attendance System.

Q2. How do I train the model?
Ans: Use the 'Train' button after capturing student photos.

Q3. Where is data stored?
Ans: Data is stored in a MySQL database and attendance in CSV files.
        """
        Label(self.faq_tab, text=faq_text, justify=LEFT, font=("Arial", 16), bg="white").pack(padx=40)

        # ==== About Tab ====
        about_text = """
👨‍💻 Developed by: Mehul Dubey
🛠️ Version: 1.0

This open-source project is a facial recognition-based attendance system using:
- Python (OpenCV, Tkinter, PIL)
- MySQL Database
- CSV for report export

📂 GitHub: https://github.com/your-repo
        """
        Label(self.about_tab, text=about_text, justify=LEFT, font=("Arial", 16), bg="white").pack(padx=40, pady=20)

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
