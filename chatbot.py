# GUI Based Rule-Based Chatbot using Python Tkinter

import tkinter as tk
from tkinter import scrolledtext

def chatbot_response():
    user_input = entry.get().lower().strip()
    chat_area.config(state=tk.NORMAL)

    if user_input == "":
        return

    chat_area.insert(tk.END, "You: " + user_input + "\n")

    if user_input == "bye":
        response = "Goodbye! Have a great day 😊"

    elif "hello" in user_input or "hi" in user_input:
        response = "Hello! How can I help you?"

    elif "how are you" in user_input:
        response = "I'm doing well, thanks for asking!"

    elif "your name" in user_input or "who are you" in user_input:
        response = "I am a simple GUI-based chatbot."

    elif "help" in user_input:
        response = "I can answer basic questions like greetings."

    else:
        response = "Sorry, I didn't understand that."

    chat_area.insert(tk.END, "Chatbot: " + response + "\n\n")
    chat_area.config(state=tk.DISABLED)
    entry.delete(0, tk.END)

def clear_chat():
    chat_area.config(state=tk.NORMAL)
    chat_area.delete("1.0", tk.END)
    chat_area.config(state=tk.DISABLED)

# Main window
window = tk.Tk()
window.title("Simple GUI Chatbot")
window.geometry("500x500")

# Chat display area
chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, state=tk.DISABLED)
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Entry field
entry = tk.Entry(window, font=("Arial", 12))
entry.pack(padx=10, pady=5, fill=tk.X)

# Buttons frame
button_frame = tk.Frame(window)
button_frame.pack(pady=5)

send_button = tk.Button(button_frame, text="Send", command=chatbot_response)
send_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="Clear Chat", command=clear_chat)
clear_button.pack(side=tk.LEFT, padx=5)

# Start GUI
window.mainloop()
