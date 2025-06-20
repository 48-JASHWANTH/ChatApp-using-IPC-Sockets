import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, filedialog

# Function to handle client connections and receive messages
def handle_client(client_socket, text_area):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            client_index = clients.index(client_socket) + 1
            text_area.config(state=tk.NORMAL)
            text_area.insert(tk.END, f"Client{client_index}: {message}\n")
            text_area.yview(tk.END)
            text_area.config(state=tk.DISABLED)
            broadcast(f"Client{client_index}: {message}", client_socket)
        except:
            client_socket.close()
            break

# Function to broadcast messages to all clients
def broadcast(message, exclude_socket):
    for client in clients:
        if client != exclude_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                clients.remove(client)

# Function to send messages from the server
def send_message(text_area, message_entry):
    message = message_entry.get()
    text_area.config(state=tk.NORMAL)
    text_area.insert(tk.END, f"Server: {message}\n")
    text_area.yview(tk.END)
    text_area.config(state=tk.DISABLED)
    message_entry.delete(0, tk.END)
    broadcast(f"Server: {message}", None)

# Function to save the chat to a file
def save_chat(text_area):
    chat_content = text_area.get("1.0", tk.END)
    if chat_content.strip():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(chat_content)

# Main function to set up the server and GUI
def main():
    global clients
    clients = []

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5555))
    server.listen(5)
    print("Server listening on port 5555...")

    root = tk.Tk()
    root.title("Server Chat Application")
    root.geometry('500x500')
    root.configure(bg='#282c34')

    text_area = scrolledtext.ScrolledText(root, state=tk.DISABLED, wrap=tk.WORD, bg="#f4f4f4", font=("Arial", 12))
    text_area.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

    message_entry = tk.Entry(root, width=50, font=("Arial", 12))
    message_entry.pack(padx=20, pady=10, fill=tk.X)

    button_frame = tk.Frame(root, bg='#282c34')
    button_frame.pack(padx=20, pady=10, fill=tk.X)

    send_button = tk.Button(button_frame, text="Send", command=lambda: send_message(text_area, message_entry), bg="#007BFF", fg="white", font=("Arial", 12), activebackground="#0056b3", activeforeground="white")
    send_button.pack(side=tk.LEFT, padx=(0, 10))

    save_button = tk.Button(button_frame, text="Save Chat", command=lambda: save_chat(text_area), bg="#28a745", fg="white", font=("Arial", 12), activebackground="#218838", activeforeground="white")
    save_button.pack(side=tk.RIGHT)

    threading.Thread(target=accept_connections, args=(server, text_area)).start()

    root.mainloop()

def accept_connections(server, text_area):
    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)
        print(f"Accepted connection from {addr}")
        threading.Thread(target=handle_client, args=(client_socket, text_area)).start()

if __name__ == "__main__":
    main()
