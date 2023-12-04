import tkinter as tk

from tkinter import (Label,
                     OptionMenu,
                     StringVar,
                     Button)

from tkinter.ttk import (Separator)

# Create the main window
root = tk.Tk()
root.title("Config Generator")

# Row 1: Label (Host OS) and dropdown
os_label = Label(root, text="Host OS")
os_label.grid(row=0, column=0, padx=5, sticky='e')
os_options = ["Ubuntu 22.04", "WSL2 on Windows 11", "MacOS"]
os_selection = tk.StringVar()
os_selection.set(os_options[0])
os_dropdown = OptionMenu(root, os_selection, *os_options)
os_dropdown.config(width=20)
os_dropdown.grid(row=0, column=1, padx=5)

# Row 2: Label (GPU) and dropdown
gpu_label = Label(root, text="GPU")
gpu_label.grid(row=1, column=0, padx=5, sticky='e')
gpu_options = ["NVIDIA", "AMD", "Intel Iris/HD Graphics"]
gpu_selection = tk.StringVar()
gpu_selection.set(gpu_options[0])
gpu_dropdown = OptionMenu(root, gpu_selection, *gpu_options)
gpu_dropdown.config(width=20)
gpu_dropdown.grid(row=1, column=1, padx=5)

# Horizontal separator
separator = Separator(root, orient='horizontal')
separator.grid(row=2, column=0, columnspan=2, sticky='ew', padx=5, pady=5)

# 'Generate' button
# Function to handle button click event
def on_generate_click(os, gpu):
    result_label.config(text=f"Generated config for {os} with {gpu} GPU")

generate_button = Button(root, text="Generate", command=lambda: on_generate_click(os_selection.get(), gpu_selection.get()))
generate_button.grid(row=3, column=0, columnspan=2, pady=2)

# Modifiable result label
result_label = Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, sticky='w', padx=2, pady=2)

# Prevent resizing
root.resizable(False, False)

# Start the GUI event loop
root.mainloop()
