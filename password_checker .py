import re
import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short (min 8 characters)")

    if len(password) >= 12:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letter")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add number")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special character")

    if len(password) < 8:
        strength = "Very Weak ❌"
    elif score <= 3:
        strength = "Weak ⚠️"
    elif score <= 5:
        strength = "Medium 🔐"
    else:
        strength = "Strong 🔥"

    return strength, feedback


def check_password():
    password = entry.get()
    if not password:
        messagebox.showwarning("Warning", "Please enter a password")
        return

    strength, feedback = check_password_strength(password)

    result_label.config(text=f"Strength: {strength}")

    feedback_text.delete("1.0", tk.END)
    if feedback:
        feedback_text.insert(tk.END, "Suggestions:\n")
        for item in feedback:
            feedback_text.insert(tk.END, f"- {item}\n")
    else:
        feedback_text.insert(tk.END, "Strong password. Good job! 💪")


def toggle_password():
    if entry.cget("show") == "*":
        entry.config(show="")
        toggle_btn.config(text="Hide Password")
    else:
        entry.config(show="*")
        toggle_btn.config(text="Show Password")


# GUI setup
root = tk.Tk()
root.title("🔐 Password Strength Checker")
root.geometry("400x350")
root.config(bg="#1e1e2f")

title = tk.Label(root, text="Password Checker", fg="cyan", bg="#1e1e2f", font=("Arial", 16, "bold"))
title.pack(pady=10)

entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
entry.pack(pady=10)

toggle_btn = tk.Button(root, text="Show Password", command=toggle_password)
toggle_btn.pack()

check_btn = tk.Button(root, text="Check Strength", command=check_password, bg="green", fg="white")
check_btn.pack(pady=10)

result_label = tk.Label(root, text="", fg="yellow", bg="#1e1e2f", font=("Arial", 12))
result_label.pack()

feedback_text = tk.Text(root, height=8, width=40)
feedback_text.pack(pady=10)

root.mainloop()
