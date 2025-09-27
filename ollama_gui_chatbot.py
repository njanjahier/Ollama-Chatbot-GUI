import ollama
import tkinter as tk
from tkinter import scrolledtext, END

# Konfiguracija

MODEL = "mistral"  # promijeni u "llama3", "gemma", itd.
SYSTEM_PROMPT = "Ti si ljubazan i šaljiv chatbot koji odgovara kratko."
HISTORY_FILE = "chat_history.txt"

# Funkcija za chat

def chat_with_ollama(user_input, messages=[]):
    # Dodavanje user input u poruke
    messages.append({"role": "user", "content": user_input})

    # Pozovivanje Ollama modela
    response = ollama.chat(
        model=MODEL,
        messages=messages
    )

    reply = response["message"]["content"]
    messages.append({"role": "assistant", "content": reply})

    # Snimanje u fajl
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"Ti: {user_input}\nBot: {reply}\n\n")

    return reply, messages

# GUI verzija

def send_message():
    user_input = entry.get()
    if not user_input.strip():
        return

    chat_area.insert(END, "Ti: " + user_input + "\n")
    entry.delete(0, END)

    global conversation
    reply, conversation = chat_with_ollama(user_input, conversation)

    chat_area.insert(END, "Bot: " + reply + "\n\n")
    chat_area.yview(END)

if __name__ == "__main__":
    # Inicijalne poruke sa system promptom
    conversation = [{"role": "system", "content": SYSTEM_PROMPT}]

    # GUI prozor
    root = tk.Tk()
    root.title("PY Chatbot")
    root.geometry("500x600")

    chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=25, state="normal")
    chat_area.pack(pady=10)

    entry = tk.Entry(root, width=50)
    entry.pack(side=tk.LEFT, padx=10, pady=10)

    send_button = tk.Button(root, text="Pošalji", command=send_message)
    send_button.pack(side=tk.RIGHT, padx=10, pady=10)

    root.mainloop()

