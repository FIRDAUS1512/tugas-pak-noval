import tkinter
from tkinter import messagebox

# Membuat jendela utama
window = tkinter.Tk()
window.title("Form Data Mahasiswa")
window.geometry('400x300')
window.configure(bg='#FFFFFF')  # Warna latar putih

# Fungsi untuk menyimpan data
def simpan_data():
    nim = "23100701".get()
    nama = "firdaus".get()
    prodi = "teknik informatika".get()
    semester = "tiga".get()
    ipk1 = "3,81".get()
    ipk2 = "4,0".get()

    # Menampilkan data dalam kotak dialog
    messagebox.showinfo(
        title="Data Tersimpan",
        message=f"Data berhasil disimpan!\n\n"
                f"NIM: {nim}\nNama: {nama}\nProdi: {prodi}\n"
                f"Semester: {semester}\nIPK Semester 1: {ipk1}\nIPK Semester 2: {ipk2}"
    )
    
# Membuat judul
label_title = tkinter.Label(window, text="Data Mahasiswa", font=("Arial", 16), bg='#FFFFFF')
label_title.grid(row=0, column=0, columnspan=2, pady=10)

# Membuat label dan entry untuk NIM
label_nim = tkinter.Label(window, text="NIM", font=("Arial", 12), bg='#FFFFFF')
label_nim.grid(row=1, column=0, sticky="w", padx=10, pady=5)
entry_nim = tkinter.Entry(window, font=("Arial", 12), width=30)
entry_nim.grid(row=1, column=1, padx=10, pady=5)

# Membuat label dan entry untuk Nama
label_nama = tkinter.Label(window, text="Nama", font=("Arial", 12), bg='#FFFFFF')
label_nama.grid(row=2, column=0, sticky="w", padx=10, pady=5)
entry_nama = tkinter.Entry(window, font=("Arial", 12), width=30)
entry_nama.grid(row=2, column=1, padx=10, pady=5)

# Membuat label dan entry untuk Prodi
label_prodi = tkinter.Label(window, text="Prodi", font=("Arial", 12), bg='#FFFFFF')
label_prodi.grid(row=3, column=0, sticky="w", padx=10, pady=5)
entry_prodi = tkinter.Entry(window, font=("Arial", 12), width=30)
entry_prodi.grid(row=3, column=1, padx=10, pady=5)

# Membuat label dan entry untuk Semester
label_semester = tkinter.Label(window, text="Semester", font=("Arial", 12), bg='#FFFFFF')
label_semester.grid(row=4, column=0, sticky="w", padx=10, pady=5)
entry_semester = tkinter.Entry(window, font=("Arial", 12), width=30)
entry_semester.grid(row=4, column=1, padx=10, pady=5)

# Membuat label dan entry untuk IPK Semester 1
label_ipk1 = tkinter.Label(window, text="IPK Semester 1", font=("Arial", 12), bg='#FFFFFF')
label_ipk1.grid(row=5, column=0, sticky="w", padx=10, pady=5)
entry_ipk1 = tkinter.Entry(window, font=("Arial", 12), width=30)
entry_ipk1.grid(row=5, column=1, padx=10, pady=5)

# Membuat label dan entry untuk IPK Semester 2
label_ipk2 = tkinter.Label(window, text="IPK Semester 2", font=("Arial", 12), bg='#FFFFFF')
label_ipk2.grid(row=6, column=0, sticky="w", padx=10, pady=5)
entry_ipk2 = tkinter.Entry(window, font=("Arial", 12), width=30)
entry_ipk2.grid(row=6, column=1, padx=10, pady=5)

# Membuat tombol SIMPAN
button_simpan = tkinter.Button(window, text="SIMPAN", font=("Arial", 12), bg='#4CAF50', fg='#FFFFFF', command=simpan_data)
button_simpan.grid(row=7, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi
window.mainloop()
