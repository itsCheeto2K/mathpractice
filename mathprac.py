import tkinter as tk
from tkinter import messagebox
import random

def taoPhepToan():
    while True:
        num1 = random.randrange(1, 1000)
        num2 = random.randrange(1, 1000)
        if num2 < num1:
            break
    return num1, num2

def kiemTraKetQua():
    global num1, num2
    user_answer = int(entry.get())
    correct_answer = num1 - num2
    if user_answer == correct_answer:
        messagebox.showinfo("Kết quả", "Bạn đã trả lời đúng!")
        num1, num2 = taoPhepToan()
        label.config(text=f"{num1} - {num2}")
        entry.delete(0, tk.END)
    else:
        messagebox.showerror("Kết quả", "Bạn đã trả lời sai! Hãy thử lại.")

        def close_messagebox(event=None):
            messagebox.destroy()

        window.bind("<Return>", close_messagebox)

num1, num2 = taoPhepToan()

window = tk.Tk()
window.title("Tập tính toán")

window.geometry("400x200")

label = tk.Label(window, text=f"{num1} - {num2}")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Kiểm tra", command=kiemTraKetQua)
button.pack()

window.mainloop()