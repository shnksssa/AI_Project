import tkinter as tk
from tkinter import scrolledtext
from chatbot import get_response  # This should import your main chatbot logic

class ChatBotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Prasana - Chatbot ")
        self.root.geometry("500x600")
        self.root.resizable(False, False)

        # Title
        self.title = tk.Label(root, text="Prasana", font=("Helvetica", 18, "bold"), bg="#4A90E2", fg="white", pady=10)
        self.title.pack(fill=tk.X)

        # Chat display area
        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Helvetica", 12), state='disabled', bg="#F4F4F4")
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Entry frame
        self.entry_frame = tk.Frame(root)
        self.entry_frame.pack(fill=tk.X, padx=10, pady=10)

        self.user_input = tk.Entry(self.entry_frame, font=("Helvetica", 12))
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.user_input.bind("<Return>", self.send_message)

        self.send_button = tk.Button(self.entry_frame, text="Send", font=("Helvetica", 12), bg="#4A90E2", fg="white", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT)

        self.bot_intro()

    def bot_intro(self):
        self.display_message("Prasana", "Hi there! I'm Prasana. Ask me anything, or type 'bye' to exit.")

    def send_message(self, event=None):
        user_msg = self.user_input.get().strip()
        if user_msg:
            self.display_message("You", user_msg)
            bot_response = get_response(user_msg)
            self.display_message("Prasana", bot_response)
            self.user_input.delete(0, tk.END)

    def display_message(self, sender, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat_area.yview(tk.END)
        self.chat_area.config(state='disabled')


if __name__ == "__main__":
    root = tk.Tk()
    gui = ChatBotGUI(root)
    root.mainloop()
