import os, platform
import customtkinter as ctk

platform_os__ = platform.platform()
platform_os = ""

if "windows" in platform_os__.lower(): platform_os = "Windows"
elif "linux" in platform_os__.lower(): platform_os = "Linux"
elif "mac" in platform_os__.lower(): platform_os = "Mac"
else:
    print("You are in an unknown os, this script probably won't work for you")

default_filename = "logs.txt"

def filename_entry_empty():
    if log_filename_entry.get() == "":
        log_filename_entry.configure(border_color="red")
        window.after(25, filename_entry_empty)
        return False
    else:
        log_filename_entry.configure(border_color="")
        return True

def start():
    if filename_entry_empty():
        if platform_os == "Windows":
            print(log_cookies_var.get())
            os.system(f"python main.py {log_cookies_var.get()} {log_filename_entry.get()}")
        elif platform_os == "Linux" or platform_os == "Mac":
            os.system(f"python3 main.py {log_cookies_var.get()} {log_filename_entry.get()}")
        else:
            os.system(f"python3 main.py {log_cookies_var.get()} {log_filename_entry.get()}")

window = ctk.CTk()
window.title("Biscuit")
window.geometry("350x250")

title_label = ctk.CTkLabel(window, text="Biscuit Cracker", font=ctk.CTkFont(family="Roboto", size=35, weight="bold"), text_color="gray")
title_label.pack(pady=20, padx=10)

log_filename_entry = ctk.CTkEntry(window, placeholder_text="Logs filename")
log_filename_entry.configure(placeholder_text="Logs filename")
log_filename_entry.pack(pady=10, padx=10, fill="x")

log_cookies_var = ctk.BooleanVar(value=True)

log_cookies_check = ctk.CTkCheckBox(window, text="Log Cookies", variable=log_cookies_var)
log_cookies_check.pack(pady=10, padx=10)

start_button = ctk.CTkButton(window, text="Start", command=start)
start_button.pack(pady=10, padx=10)

window.mainloop()