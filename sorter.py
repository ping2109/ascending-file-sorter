import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk  # Make sure to install the Pillow library: pip install Pillow

def sort_and_rename_files(directory):
    # Get a list of files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    # Sort files based on modification time
    files.sort(key=lambda x: os.path.getmtime(os.path.join(directory, x)))

    # Rename files in ascending order starting from 0
    for index, file_name in enumerate(files):
        original_path = os.path.join(directory, file_name)
        _, file_extension = os.path.splitext(file_name)
        new_name = f"{index:03d}{file_extension}"  # 3 digits padding for index
        new_path = os.path.join(directory, new_name)
        os.rename(original_path, new_path)
        print(f"Renamed: {file_name} -> {new_name}")

def select_directory():
    directory_path = filedialog.askdirectory(title="Select Directory")
    if directory_path:
        directory_var.set(directory_path)
        result_label.config(text="")

def start_processing():
    directory_path = directory_var.get()
    if directory_path:
        sort_and_rename_files(directory_path)
        result_label.config(text="Files sorted and renamed successfully.")

# GUI setup
root = tk.Tk()
root.title("File Sorter and Renamer")

# Load and display a custom logo image
base_dir = os.path.dirname(__file__)
logo_path = os.path.join(base_dir, './icon.png') # Replace with the path to your logo image
if os.path.exists(logo_path):
    logo_image = Image.open(logo_path)
    logo_image = logo_image.resize((128, 128), Image.ANTIALIAS)  # Resize the image
    logo_image = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(root, image=logo_image)
    logo_label.image = logo_image  # Keep a reference to prevent garbage collection
    logo_label.pack(pady=10)

# Add a custom title below the icon
title_label = tk.Label(root, text="     Sort files in a folder based on their last modified date and rename in ascending order.     \nuwu made by tozn owo", font=("Helvetica", 16))
title_label.pack()

# Add a button to select the directory
select_button = tk.Button(root, text="Select Directory", command=select_directory)
select_button.pack(pady=10)

# Add an entry to display the selected directory
directory_var = tk.StringVar()
directory_entry = tk.Entry(root, textvariable=directory_var, state="readonly")
directory_entry.pack(pady=10)

# Add a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Add a "Start" button
start_button = tk.Button(root, text="Start", command=start_processing)
start_button.pack(pady=10)

# Run the GUI
root.mainloop()
