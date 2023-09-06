from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
import time

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.configure(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, width=280, text='', fill=THEME_COLOR,
                                                     font=("Arial", 15, "normal"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_img = PhotoImage(file='images/true.png')
        self.true_button = Button(image=self.true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        self.false_img = PhotoImage(file='images/false.png')
        self.false_button = Button(image=self.false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        quiz_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=quiz_text)

    def true_pressed(self):
        if self.quiz.still_has_questions():
            self.feedback(self.quiz.check_answer('True'))
            self.get_next_question()

    def false_pressed(self):
        if self.quiz.still_has_questions():
            self.get_next_question()
            self.feedback(self.quiz.check_answer('False'))

    def feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg='green')
            self.score_label.configure(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.configure(bg='red')

        self.window.after(300, self.blink)

    def blink(self):
        self.canvas.configure(bg='white')