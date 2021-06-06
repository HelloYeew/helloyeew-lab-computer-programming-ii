import tkinter as tk
import tkinter.ttk as ttk
from datetime import datetime


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Digital Clock")
        self.geometry("400x100")
        self.style = ttk.Style()
        self.style.configure(".", font=("Arial", 24))
        self.str_date = tk.StringVar()
        self.str_time = tk.StringVar()
        self.date = ttk.Label(textvariable=self.str_date)
        self.time = ttk.Label(textvariable=self.str_time)
        self.update_time()
        self.date.pack()
        self.time.pack()
        self.button = ttk.Button(text="Quit", command=self.quit)
        self.button.pack()

    def update_time(self):
        date_now = datetime.now().strftime("%d %B %Y")
        time_now = datetime.now().strftime("%H:%M:%S")
        self.str_date.set(date_now)
        self.str_time.set(time_now)
        self.after(1000, self.update_time)

    def quit(self):
        self.destroy()
    
    def run(self):
        self.mainloop()


if __name__ == "__main__":
    app = Application()
    app.mainloop()
