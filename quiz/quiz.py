import tkinter as tk
from tkinter import messagebox

# Quiz data
questions = [
    {
        "question": "A train 240 meters long passes a pole in 24 seconds. What is the speed of the train in km/hr?",
        "options": ["30", "36", "45", "54"],
        "answer": "36"
    },
    {
        "question": "The ratio of ages of two people is 3:5. Five years ago, their ages were 15 and 25. What is their present age?",
        "options": ["20 and 30", "25 and 35", "30 and 50", "35 and 55"],
        "answer": "20 and 30"
    },
    {
        "question": "If A is the brother of B, B is the sister of C, and C is the father of D, how is A related to D?",
        "options": ["Uncle", "Father", "Brother", "Grandfather"],
        "answer": "Uncle"
    },
    {
        "question": "Choose the correct synonym for the word 'benevolent':",
        "options": ["Kind", "Cruel", "Lazy", "Generous"],
        "answer": "Kind"
    },
    {
        "question": "Which type of inheritance allows a class to inherit from multiple classes?",
        "options": ["Single inheritance", "Multiple inheritance", "Multilevel inheritance", "Hierarchical inheritance"],
        "answer": "Multiple inheritance"
    }
]



class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.current_question_index = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", wraplength=400, font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.options_var = tk.StringVar()

        self.options_frame = tk.Frame(root)
        self.options_frame.pack()

        self.option_buttons = []
        for _ in range(4):
            button = tk.Radiobutton(self.options_frame, text="", variable=self.options_var, font=("Arial", 12),
                                    value="", tristatevalue="0")
            button.pack(anchor="w", pady=5)
            self.option_buttons.append(button)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer, font=("Arial", 12))
        self.submit_button.pack(pady=20)

        self.update_question()

    def update_question(self):
        if self.current_question_index < len(questions):
            question_data = questions[self.current_question_index]
            self.question_label.config(text=question_data["question"])
            self.options_var.set(None)

            for i, option in enumerate(question_data["options"]):
                self.option_buttons[i].config(text=option, value=option)
        else:
            self.show_final_score()

    def check_answer(self):
        selected_option = self.options_var.get()
        if not selected_option:
            messagebox.showwarning("Warning", "Please select an option")
            return

        correct_answer = questions[self.current_question_index]["answer"]
        if selected_option == correct_answer:
            self.score += 1

        self.current_question_index += 1
        self.update_question()

    def show_final_score(self):
        messagebox.showinfo("Quiz Completed", f"Your score: {self.score}/{len(questions)}")
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
