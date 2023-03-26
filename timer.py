import tkinter as tk

class Timer:
    def __init__(self, window):
        self.window=window
        self.window.title("Таймер")
        self.minutes = tk.StringVar()
        self.seconds = tk.StringVar()
        self.minutes.set("00")
        self.seconds.set("00")
        self.timer_running = False

        self.label = tk.Label(self.window, textvariable=self.minutes, font=("Arial", 24), fg="black")
        self.label.pack()
        self.label = tk.Label(self.window, text=":", font=("Arial", 24), fg="black")
        self.label.pack()
        self.label = tk.Label(self.window, textvariable=self.seconds, font=("Arial", 24), fg="black")
        self.label.pack()
        self.start_button = tk.Button(self.window, text="Старт", command=self.start_timer)
        self.start_button.pack(pady=10)
        self.stop_button = tk.Button(self.window, text="Стоп", command=self.stop_timer)
        self.stop_button.pack(pady=10)

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.remaining_time = int(self.minutes.get()) * 60 + int(self.seconds.get())
            self.update_timer()

    def update_timer(self):
        minutes, seconds = divmod(self.remaining_time, 60)
        self.minutes.set("{:02d}".format(minutes))
        self.seconds.set("{:02d}".format(seconds))
        if self.remaining_time > 0 and self.timer_running:
            self.remaining_time -= 1
            self.window.after(1000, self.update_timer)
        elif self.remaining_time == 0 and self.timer_running:
            self.timer_running = False
            self.window.bell()

    def stop_timer(self):
        self.timer_running = False


if __name__ == "__main__":
    root = tk.Tk()
    timer = Timer(root)
    root.mainloop()