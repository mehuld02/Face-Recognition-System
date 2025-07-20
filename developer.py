from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Developer Info")

        # ===== Background Image =====
        bg_img = Image.open("images/background.jpg")
        bg_img = bg_img.resize((1300, 710), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_img)

        bg_label = Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # ===== Title =====
        title_lbl = Label(self.root, text="Meet the Developer", font=("Helvetica", 35, "bold"),
                          bg="#000000", fg="white")
        title_lbl.place(x=0, y=0, width=1300, height=60)

        # ===== Developer Frame =====
        main_frame = Frame(self.root, bg="white", bd=4, relief=RIDGE)
        main_frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=650, height=500)

        # ===== Developer Image =====
        dev_img = Image.open("images/dev.jpeg")
        dev_img = dev_img.resize((150, 150), Image.LANCZOS)
        self.dev_photo = ImageTk.PhotoImage(dev_img)
        dev_label = Label(main_frame, image=self.dev_photo, bd=2)
        dev_label.place(x=20, y=20)

        # ===== Text Info =====
        Label(main_frame, text="Mehul Dubey", font=("Arial", 22, "bold"), fg="#333", bg="white").place(x=190, y=30)
        Label(main_frame, text="Full Stack Web Developer", font=("Arial", 16), bg="white", fg="black").place(x=190, y=70)
        Label(main_frame, text="Python | MERN | AI | ML", font=("Arial", 14), bg="white", fg="#555").place(x=190, y=100)

        # ===== Buttons =====
        email_btn = Button(main_frame, text="📧 Email Me", font=("Arial", 13, "bold"), bg="#0A66C2", fg="white",
                           cursor="hand2", width=15, command=lambda: self.open_email())
        email_btn.place(x=60, y=180)

        linkedin_btn = Button(main_frame, text="💼 LinkedIn", font=("Arial", 13, "bold"), bg="#0077B5", fg="white",
                              cursor="hand2", width=15, command=lambda: self.open_linkedin())
        linkedin_btn.place(x=240, y=180)

        github_btn = Button(main_frame, text="💻 GitHub", font=("Arial", 13, "bold"), bg="#24292e", fg="white",
                            cursor="hand2", width=15, command=lambda: self.open_github())
        github_btn.place(x=420, y=180)

        # ===== Bottom Image =====
        bottom_img = Image.open("images/dev1.jpg")
        bottom_img = bottom_img.resize((600, 250), Image.LANCZOS)
        self.bottom_photo = ImageTk.PhotoImage(bottom_img)

        bottom_lbl = Label(main_frame, image=self.bottom_photo, bd=2)
        bottom_lbl.place(x=25, y=240)

    def open_email(self):
        webbrowser.open("mailto:support@example.com")

    def open_linkedin(self):
        webbrowser.open("https://www.linkedin.com/in/your-profile")  

    def open_github(self):
        webbrowser.open("https://github.com/your-username")  


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
