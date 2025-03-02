import tkinter as tk
from tkinter import messagebox
quiz_data = [
      {
       "question": "What is the capital of France?",
       "options": ["Paris","London","Rome","Berlin"],
       "answer": "Paris"
      },
      {
      "question": "Which planet is known as the Red Planet?",
      "options": ["Earth","Mars","Jupiter","Venus"],
      "answer": "Mars"
      },
      {
      "question": "What is the largest ocean on Earth?",
      "options": ["Atlantic ocean","Indian","Artic Ocean","Pacific"],
      "answer": "Pacific Ocean"
      }
]

class QuizApp:

     def next_question(self):
         pass

     def display_question(self):

         question_data = quiz_data[self.current_question]

         self.question_label.config(text=question_data["question"])

         self.selected_option.set(None)

         for i, option in enumerate(question_data["options"]):

             self.option_buttons[i].config(text=option, value=option)

     def __init__(self, root):
         self.root = root
         self.root.title("Quiz App")

         self.current_question = 0
         self.score = 0

         self.question_label = tk.Label(root, text = "", font = ("Arial", 16), wraplength = 400)
         self.question_label.pack(pady=20)

         self.selected_option = tk.StringVar()

         self.option_buttons = []

         for i in range(4):
             btn = tk.Radiobutton(root, text = "", variable=self.selected_option, value="", font=("Arial",14))
             btn.pack(anchor="w")
             self.option_buttons.append(btn)

         self.next_button = tk.Button(root, text = "Next", command = self.next_question, font=("Arial",14))
         self.next_button.pack(pady=20)

         self.display_question()

def main():

    root = tk.Tk()

    app = QuizApp(root)

    root.mainloop()

main()
