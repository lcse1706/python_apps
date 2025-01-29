import tkinter as tk
import tkinter.messagebox as msg

root = tk.Tk()
root.title("Hello world")
root.geometry("400x400")

# Create a label widget
label = tk.Label(root, text="Welcome to my App.", font=("Helvetica", 20))
label.pack(pady=10)

# Create an input widget
entry_label = tk.Label(root, text="Enter Your Name")
entry_label.pack()
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Create a button widget
def onClick():
    name = entry.get()
    if name:
        msg.showinfo("Hello", f"Hello {name}")
        
    else:
        label = tk.Label(root, text="Please enter your name.")
        label.pack()
        
button = tk.Button(root, text="Submit", command=onClick)
button.pack(pady=10)

# CheckBox
checkbox_var = tk.BooleanVar()

checkbox = tk.Checkbutton(root, text="Check to subscribe to our newsletter", variable=checkbox_var)
checkbox.pack(pady=10)

# Radio Button

radio_label = tk.Label(root, text="Choose your favorite programming language:")
radio_label.pack()

favorite_lang = tk.StringVar(value="None")

languages = [("Python", "Python"), ("JavaScript", "JavaScript"), ("Java", "Java"), ("C++", "C++")]

for text, lang in languages:
    radio = tk.Radiobutton(root, text=text, variable=favorite_lang, value=lang)
    radio.pack()
    
root.mainloop()