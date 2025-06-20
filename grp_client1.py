import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, filedialog
from tkinter import messagebox

# Function to handle receiving messages
def receive_messages(client_socket, text_area):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            text_area.config(state=tk.NORMAL)
            text_area.insert(tk.END, f"{message}\n")
            text_area.yview(tk.END)
            text_area.config(state=tk.DISABLED)
        except:
            messagebox.showerror("Error", "An error occurred!")
            client_socket.close()
            break

# Function to send messages
def send_message(client_socket, message_entry, text_area):
    message = message_entry.get()
    client_socket.send(message.encode('utf-8'))
    text_area.config(state=tk.NORMAL)
    text_area.insert(tk.END, f"You: {message}\n")
    text_area.yview(tk.END)
    text_area.config(state=tk.DISABLED)
    message_entry.delete(0, tk.END)

# Function to save the chat to a file
def save_chat(text_area):
    chat_content = text_area.get("1.0", tk.END)
    if chat_content.strip():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(chat_content)

# Main function to set up the GUI and connect to the server
def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 5555))

    root = tk.Tk()
    root.title("Client Chat Application")
    root.geometry('500x500')
    root.configure(bg='#282c34')

    text_area = scrolledtext.ScrolledText(root, state=tk.DISABLED, wrap=tk.WORD, bg="#f4f4f4", font=("Arial", 12))
    text_area.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

    message_entry = tk.Entry(root, width=50, font=("Arial", 12))
    message_entry.pack(padx=20, pady=10, fill=tk.X)

    button_frame = tk.Frame(root, bg='#282c34')
    button_frame.pack(padx=20, pady=10, fill=tk.X)

    send_button = tk.Button(button_frame, text="Send", command=lambda: send_message(client_socket, message_entry, text_area), bg="#007BFF", fg="white", font=("Arial", 12), activebackground="#0056b3", activeforeground="white")
    send_button.pack(side=tk.LEFT, padx=(0, 10))

    save_button = tk.Button(button_frame, text="Save Chat", command=lambda: save_chat(text_area), bg="#28a745", fg="white", font=("Arial", 12), activebackground="#218838", activeforeground="white")
    save_button.pack(side=tk.RIGHT)

    threading.Thread(target=receive_messages, args=(client_socket, text_area)).start()

    root.mainloop()

if __name__ == "__main__":
    main()
