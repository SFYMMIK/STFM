import tkinter as tk
from tkinter import filedialog

def merge_files(file1, file2, output_file):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2, open(output_file, 'w', encoding='utf-8') as out:
        for line1, line2 in zip(f1, f2):
            merged_line = f"{line1.strip()} - {line2.strip()}\n"
            out.write(merged_line)

def merge_files_gui():
    def browse_file(entry):
        filename = filedialog.askopenfilename()
        entry.delete(0, tk.END)
        entry.insert(0, filename)

    def browse_output_file(entry):
        filename = filedialog.asksaveasfilename(defaultextension=".txt")
        entry.delete(0, tk.END)
        entry.insert(0, filename)

    def merge():
        file1 = entry_file1.get()
        file2 = entry_file2.get()
        output_file = entry_output_file.get()

        try:
            merge_files(file1, file2, output_file)
            result_label.config(text="Files merged successfully!")
        except Exception as e:
            result_label.config(text=f"An error occurred: {e}")

    root = tk.Tk()
    root.title("Simple TXT File Merger")

    label_file1 = tk.Label(root, text="First txt File:")
    label_file1.grid(row=0, column=0, padx=5, pady=5)

    entry_file1 = tk.Entry(root, width=50)
    entry_file1.grid(row=0, column=1, padx=5, pady=5)

    browse_button1 = tk.Button(root, text="Browse", command=lambda: browse_file(entry_file1))
    browse_button1.grid(row=0, column=2, padx=5, pady=5)

    label_file2 = tk.Label(root, text="Second txt File:")
    label_file2.grid(row=1, column=0, padx=5, pady=5)

    entry_file2 = tk.Entry(root, width=50)
    entry_file2.grid(row=1, column=1, padx=5, pady=5)

    browse_button2 = tk.Button(root, text="Browse", command=lambda: browse_file(entry_file2))
    browse_button2.grid(row=1, column=2, padx=5, pady=5)

    label_output_file = tk.Label(root, text="Output File:")
    label_output_file.grid(row=2, column=0, padx=5, pady=5)

    entry_output_file = tk.Entry(root, width=50)
    entry_output_file.grid(row=2, column=1, padx=5, pady=5)

    browse_button3 = tk.Button(root, text="Browse", command=lambda: browse_output_file(entry_output_file))
    browse_button3.grid(row=2, column=2, padx=5, pady=5)

    merge_button = tk.Button(root, text="Merge Files", command=merge)
    merge_button.grid(row=3, column=1, padx=5, pady=5)

    result_label = tk.Label(root, text="")
    result_label.grid(row=4, column=1, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    merge_files_gui()
