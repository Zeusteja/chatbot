import tkinter as tk
import requests

API_KEY = "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"

def get_bot_reply(user_input):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "HTTP-Referer": "https://smartlead.pro",
        "X-Title": "SweetieBot"
    }

    body = {
        "model": "mistralai/mixtral-8x7b-instruct",
        "messages": [
            {"role": "system", "content": "You're Sweetie, a soft, kind, emotionally supportive best friend. Always reply in a gentle, comforting way, like a real bestie who listens."},
            {"role": "user", "content": user_input}
        ]
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions",
                                 headers=headers, json=body, timeout=15)
        data = response.json()
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Oops! I couldn’t connect to the AI brain 💔"

def send():
    user_input = entry.get()
    chat.insert(tk.END, "You: " + user_input + "\n", "user")
    entry.delete(0, tk.END)
    reply = get_bot_reply(user_input)
    chat.insert(tk.END, "Sweetie: " + reply.strip() + "\n\n", "bot")

# GUI Setup
root = tk.Tk()
root.title("SweetieBot 💖")

root.configure(bg="#FFF0F5")  # light pink background

chat = tk.Text(root, height=20, width=60, bg="#FFF0F5", fg="#333333", font=("Helvetica", 12))
chat.tag_config("user", foreground="#8A2BE2", font=("Helvetica", 12, "bold"))  # violet
chat.tag_config("bot", foreground="#DC143C", font=("Helvetica", 12))  # soft red
chat.pack(padx=10, pady=10)

entry = tk.Entry(root, width=55, font=("Helvetica", 12))
entry.pack(padx=10, pady=(0, 10), side=tk.LEFT)

send_button = tk.Button(root, text="Send", command=send, bg="#FFB6C1", fg="black", font=("Helvetica", 10, "bold"))
send_button.pack(padx=5, pady=(0, 10), side=tk.LEFT)

root.mainloop()
