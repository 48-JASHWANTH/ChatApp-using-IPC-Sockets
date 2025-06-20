# 💬 Chat Application using IPC Sockets

A real-time chat application implemented in **Python** using socket programming for **Inter-Process Communication (IPC)**. This application allows **multiple clients** to connect to a **central server** and exchange messages in a group chat environment.

---

## ✨ Features

* 👥 **Multi-client support**: Multiple clients can connect to the server simultaneously
* ⚡ **Real-time messaging**: Instant message delivery between connected clients
* 🖼️ **Graphical User Interface**: Built with Tkinter for both server and client applications
* 🕘 **Chat history**: View all messages exchanged during the session
* 💾 **Save functionality**: Option to save chat history to a text file

---

## 🧩 Components

### 🖥️ Server (`grp_server.py`)

* 🧭 Acts as the central hub for all communications
* 📡 Manages client connections and broadcasts messages
* 👨‍💻 Provides a GUI for server administrators to monitor and participate in chats
* 💾 Allows saving the chat history

### 👤 Clients (`grp_client1.py`, `grp_client2.py`)

* 🔌 Connect to the server to join the chat room
* 📬 Send and receive messages in real-time
* 🖥️ Display messages from all participants

---

## 📦 Requirements

* 🐍 Python 3.x
* 🖼️ Tkinter (usually pre-installed with Python)
* 🧵 Threading library (standard Python library)
* 🔌 Socket library (standard Python library)

---

## 🚀 How to Run

1. ▶️ **Start the server**:

   ```bash
   python grp_server.py
   ```

2. ▶️ **Start one or more clients**:

   ```bash
   python grp_client1.py
   ```

   or

   ```bash
   python grp_client2.py
   ```

3. 💬 Enter messages in the client window to participate in the chat.

---

## 🌐 Network Configuration

* 📍 The server listens on **port 5555**
* 🌍 By default, the server binds to **all network interfaces** (`0.0.0.0`)
* 🔑 Clients need to know the **server's IP address** to connect

---

## ⚙️ Implementation Details

* 🔒 Uses **TCP sockets** for reliable communication
* 🧵 Implements **threading** to handle multiple client connections simultaneously
* 🖼️ Uses **Tkinter** for the graphical user interface
* 🌐 Messages are encoded/decoded using **UTF-8**

---
