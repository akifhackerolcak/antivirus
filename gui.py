import tkinter as tk
from tkinter import filedialog, messagebox
from scanner import scan_directory, scan_file

def klasor_sec():
    klasor = filedialog.askdirectory()
    if klasor:
        sonuc = scan_directory(klasor)
        messagebox.showinfo("Tarama Sonucu", sonuc)

def dosya_sec():
    dosya = filedialog.askopenfilename()
    if dosya:
        sonuc = scan_file(dosya)
        messagebox.showinfo("Dosya Tarama Sonucu", sonuc)

def baslat_gui():
    pencere = tk.Tk()
    pencere.title("Basit Antivirüs")
    pencere.geometry("300x200")

    btn1 = tk.Button(pencere, text="Klasör Tara", command=klasor_sec)
    btn1.pack(pady=20)

    btn2 = tk.Button(pencere, text="Dosya Tara", command=dosya_sec)
    btn2.pack(pady=10)

    pencere.mainloop()
