import os
import csv
import tkinter as tk

# Move to the directory where this script is located
os.chdir(os.path.dirname(os.path.realpath(__file__)))

data = []
fields = []

def create_field(default_command=None):
    new_field1 = tk.Entry(root)
    new_field1.insert(0, default_command or '')  # Insert default text if provided
    new_field1.grid(row=len(fields)+2, column=1)
    new_field2 = tk.Entry(root)
    new_field2.grid(row=len(fields)+2, column=2)
    fields.append((new_field1, new_field2))

def add_field():
    create_field()

def remove_field():
    if len(fields) > 0:
        field_to_remove = fields.pop()
        field_to_remove[0].destroy()
        field_to_remove[1].destroy()

def export_to_csv():
    for field in fields:
        command = field[0].get()  # Now represents command
        element = field[1].get()  # Now represents element
        if command and element:  # Check if both fields are non-empty
            data.append([command, element])
    
    with open('scenario.csv', 'w', newline='', encoding='utf-8') as f:  # Updated file name
        writer = csv.writer(f)
        writer.writerow(['command', 'element'])  # Add headers
        writer.writerows(data)

    root.destroy()  # Close the program

root = tk.Tk()

button_add = tk.Button(root, text="Add Record", command=add_field)
button_add.grid(row=0, column=0)

button_remove = tk.Button(root, text="Remove Record", command=remove_field)
button_remove.grid(row=0, column=1)

button_export = tk.Button(root, text="Export to CSV", command=export_to_csv)
button_export.grid(row=0, column=2)

# Create headers
header1 = tk.Label(root, text="Command")
header1.grid(row=1, column=1)
header2 = tk.Label(root, text="Element")
header2.grid(row=1, column=2)

# Create initial 2 fields with default commands
create_field(default_command='question')
create_field(default_command='answer')

root.mainloop()
