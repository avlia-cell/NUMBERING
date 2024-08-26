import tkinter as tk
from tkinter import messagebox

def cek_angka():
    try:
        angka = float(entry_angka.get())
        if angka > 0:
            hasil = "Angka Positif"
        elif angka == 0:
            hasil = "Angka Nol"
        else:
            hasil = "Angka Negatif"
        messagebox.showinfo("Hasil", hasil)
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

# Membuat jendela utama
root = tk.Tk()
root.title("Cek Kondisi Angka")
root.geometry("300x150")  # Ukuran jendela

# Label dan input untuk angka
label_angka = tk.Label(root, text="Tulis Sebuah Angka:")
label_angka.grid(row=0, column=0, padx=10, pady=10, sticky="w")

entry_angka = tk.Entry(root, width=20)
entry_angka.grid(row=0, column=1, padx=10, pady=10)

# Tombol untuk memeriksa kondisi angka
button_cek = tk.Button(root, text="Cek Kondisi Angka", command=cek_angka)
button_cek.grid(row=1, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi
root.mainloop()
