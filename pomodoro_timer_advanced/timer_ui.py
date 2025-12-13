from tkinter import *

class PomodoroUI:
    def __init__(self, settings):
        self.s = settings

        self.window = Tk()
        self.window.title("Let's Pomodoro!")
        self.window.config(padx=50, pady=100, bg=self.s.COTTON_ROSE)

        self.timer_label = Label(text="Pomodoro", fg=self.s.COTTON_ROSE, bg=self.s.BG_COLOR, font=(self.s.FONT_NAME, 45, "bold"))
        self.timer_label.grid(column=1, row=0)

        self.canvas = Canvas(width=307, height=307, bg=self.s.COTTON_ROSE, highlightthickness=0)
        self.computer_img = PhotoImage(file="computer_image.png")
        self.canvas.create_image(153, 153, image=self.computer_img)
        self.timer_text = self.canvas.create_text(156, 100, text="00:00", fill=self.s.TEXT_COLOR, font=(self.s.FONT_NAME, 25, "bold"))
        self.canvas.grid(column=1, row=1)

        self.start_button = Button(text="Start", fg=self.s.TEXT_COLOR, font=(self.s.FONT_NAME, 10, "normal"), highlightthickness=0)
        self.start_button.grid(column=0, row=2)

        self.reset_button = Button(text="Reset", fg=self.s.TEXT_COLOR, font=(self.s.FONT_NAME, 10, "normal"), highlightthickness=0)
        self.reset_button.grid(column=2, row=2)

        self.check_marks = Label(fg=self.s.MUTED_TEAL, bg=self.s.COTTON_ROSE)
        self.check_marks.grid(column=1, row=3)

    # UI update method
    def set_time(self, mm: str, ss: str):
        self.canvas.itemconfig(self.timer_text, text=f"{mm}:{ss}")

    def set_session(self, title: str, color: str):
        self.timer_label.config(text=title, fg=color)

    def set_marks(self, marks: str):
        self.check_marks.config(text=marks)

    # connect button to external handler
    def bind_start(self, handler):
        self.start_button.config(command=handler)

    def bind_reset(self, handler):
        self.reset_button.config(command=handler)

    def run(self):
        self.window.mainloop()