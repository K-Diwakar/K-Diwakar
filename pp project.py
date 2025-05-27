import tkinter as tk
from time import strftime
from datetime import datetime

def time():
    current_time = strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    root.after(1000, time)

def date():
    current_date = datetime.now().strftime('%A, %d %B %Y')
    date_label.config(text=current_date)

# Setup the main window
root = tk.Tk()
root.title('Minimal Student Clock')
root.configure(bg='black')

# Clock display
clock_label = tk.Label(root, font=('Helvetica', 60), fg='white', bg='black')
clock_label.pack(pady=20)

# Date display
date_label = tk.Label(root, font=('Helvetica', 20), fg='gray', bg='black')
date_label.pack(pady=10)

# Initialize the time and date functions
time()
date()

# Run the clock
root.mainloop() 