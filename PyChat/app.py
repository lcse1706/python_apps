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



root.mainloop()