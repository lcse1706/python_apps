import tkinter as tk
import pymongo

# Connect to MongoDB

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["PyChat"]
messages_col = db["messages"]

# Tkinter GUI

root = tk.Tk()
root.title("PyChat")
root.geometry("400x400")


entry = tk.Entry(root, width=40)
entry.pack(pady=5)

def sendMessage(message):
  if entry.get():
    messages_col.insert_one({"text": entry.get()})
    entry.delete(0, tk.END)
    # updateMessages()
    
send_button = tk.Button(root, text="Send", command=lambda: sendMessage(entry.get()))
send_button.pack(pady=5)

messages_label = tk.Label(root, text="Messages:\n", justify="left")
messages_label.pack(pady=5)

# messages = tk.Text(root, width=50, height=20)
# messages.pack(pady=5)



def updateMessages():
  messages = list(messages_col.find().sort("_id", -1).limit(10)) 
  messages_label.config(text="Messages:\n"+ "\n".join(f"- {message['text']}" for message in messages))
  root.after(1000, updateMessages)
  

updateMessages()
root.mainloop()