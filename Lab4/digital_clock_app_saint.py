import tkinter as tk
import tkinter.ttk as ttk
from datetime import datetime


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Digital Clock")
        self.geometry("400x100")
        self.display = ttk.Style()
        self.display.configure(".", font=("Arial", 24))
        self.str_date = tk.StringVar()
        self.str_time = tk.StringVar()
        self.label_date = ttk.Label(textvariable=self.str_date)
        self.label_time = ttk.Label(textvariable=self.str_time)
        self.update_time()
        # self.str_date.set("***Current Date***")
        # self.str_time.set("***Current Time***")
        # self.label_date = tk.Label(self, text="date")
        self.label_date.pack()
        # self.label_time = tk.Label(self, text="time")
        self.label_time.pack()
        self.button_quit = ttk.Button(text="Quit", command=self.quit())
        self.button_quit.pack()

    def update_time(self):
        present_date = datetime.now().strftime("%d %B %Y")
        present_time = datetime.now().strftime("%H: %M: %S")
        self.str_time.set(present_time)
        self.str_date.set(present_date)
        self.after(1000, self.update_time)

    def run(self):
        self.mainloop()

    def quit(self):
        self.destroy()




if __name__ == "__main__":
    app = Application()
    app.mainloop()
