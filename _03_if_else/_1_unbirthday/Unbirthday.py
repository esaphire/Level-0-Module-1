from tkinter import messagebox, simpledialog, Tk
window = Tk()
if __name__ == '__main__':
    answer = simpledialog.askstring(title="What is your birthday?",prompt="Respond in mm/dd")
    if answer == "06/10":
        messagebox.showinfo(title="Computer",message="Happy Birthday!")
    else:
        messagebox.showinfo(title="Computer",message="A very merry unbirthday to you!")
