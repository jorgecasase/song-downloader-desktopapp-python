import os
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import font
import SongDownloader
import sys

current_dir = os.getcwd()
download_dir = os.path.join(current_dir, "DjWAV")

def procesar_url():
    url = url_entry.get()
    if url:
        titulo = SongDownloader.descargar_audio(url, download_dir)
        if titulo:
            url_entry.delete(0, tk.END)
            mensaje_label.config(text=f"{titulo} se ha descargado con éxito")
            return 0
    mensaje_label.config(text=f"ERROR")

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    window.geometry(f'{width}x{height}+{x}+{y}')
    
root = tk.Tk()
center_window(root, 600, 250)
root.resizable(width=False, height=False)

root.title("DjWAV for DjDrag0n")
foto_path = os.path.join(sys._MEIPASS, 'logo.ico')
root.iconbitmap(foto_path)

image_path = os.path.join(sys._MEIPASS, 'background.png')
bg = PhotoImage(file=image_path)

my_canvas = Canvas(root, width=600, height=250)
my_canvas.pack(fill="both", expand=True)
my_canvas.create_image(0,0,image=bg, anchor="nw")

#######my_canvas.create_text(300, 40, text="DjWAV", font=('Helvetica', 50), fill="white")
title_image_path = os.path.join(sys._MEIPASS, 'title.png')
title_image = PhotoImage(file=title_image_path)
my_canvas.create_image(20, 0, image=title_image, anchor="nw")

url_label = tk.Label(text="Youtube URL")
url_label_window = my_canvas.create_window(50, 120, anchor="nw", window=url_label)

url_entry = tk.Entry(width=50)
url_entry_window = my_canvas.create_window(150, 120, anchor="nw", window=url_entry)

procesar_button = tk.Button(text="descargar", command=procesar_url)
procesar_button_window = my_canvas.create_window(260, 160, anchor="nw", window=procesar_button)

mensaje_label = tk.Label(text='', fg="black")
mensaje_label_window = my_canvas.create_window(50, 200, anchor="nw", window=mensaje_label)

root.mainloop()