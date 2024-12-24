import tkinter as tk

mainWindow = tk.Tk()
mainWindow.geometry("400x300")

# Create a Listbox widget
listbox = tk.Listbox(mainWindow)
listbox.pack(side="left", fill="both", expand=True)

# Create a Scrollbar widget for the Listbox
scrollbar = tk.Scrollbar(mainWindow, command=listbox.yview)
scrollbar.pack(side="right", fill="y")

# Link the scrollbar to the Listbox widget
listbox.config(yscrollcommand=scrollbar.set)

# Add some items to the Listbox
for i in range(30):
    listbox.insert(tk.END, f"Item {i + 1}")

mainWindow.mainloop()
