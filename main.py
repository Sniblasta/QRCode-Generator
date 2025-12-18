import qrcode
import tkinter as tk
from tkinter import messagebox

def create_qr():
    data = entry.get()
    if not data:
        messagebox.showwarning("Input Error", "Please enter some data to generate QR code.")
        return
    img = qrcode.make(data)
    img.save("qrcode.png")
    messagebox.showinfo("Success", "QR code generated and saved as qrcode.png")

window = tk.Tk()
window.title("QR Code Generator")
window.geometry("200x150")

label = tk.Label(window, text="Enter Your Link:")
label.pack(pady=5)

entry = tk.Entry(window, width=30)
entry.pack(pady=5)

button = tk.Button(window, text="Generate QR Code", command=create_qr)
button.pack(pady=10)

window.mainloop()


