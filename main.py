from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *
from PIL import ImageTk, Image

hunians = []
hunians.append(Apartemen("Dicki Fathurohman", 3, 3, "Jl. M.H. Thamrin No.15 Jakarta Pusat, Jakarta."))
hunians.append(Rumah("Gatsby Del Rey", 5, 2, "Jl. Kejawan Putih No.21 Kota Surabaya, Jawa Timur."))
hunians.append(Indekos("Mr. Cavill", "Timothee Chalamet", "Jl. Gatot Subroto No.6, Kota Bandung, Jawa Barat."))
hunians.append(Rumah("Minatozaki Sana", 1, 4, "Jl. Pd Indah No.12 Jakarta Selatan, Jakarta."))

root = Tk()
root.title("Praktikum DPBO Python")
root.geometry("400x400")

Landing = Label(root, text="Selamat Datang", padx=10, pady=10)
Landing.pack(padx=10, pady=10)

gambar = ImageTk.PhotoImage(Image.open("Residence.png").resize((200,200)))

foto = Label(root, image = gambar)
foto.pack()

ResidenPage = Button(root, text="Daftar Residen", command=lambda : listHunians(), padx=10, pady=10, width=40)
ResidenPage.pack()

def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)
    
    d_summary = Label(d_frame, text="Summary\n" + hunians[index].get_detail() + hunians[index].get_alamat() + hunians[index].get_summary() + "\n" + hunians[index].get_dokumen(), anchor="w", justify=LEFT).grid(row=0, column=0, sticky="w")

    btn = LabelFrame(top, padx=0, pady=0)
    btn.pack(padx=10, pady=10)
    b_close = Button(btn, text="Close", command=top.destroy)
    b_close.grid(row=0, column=0)

def listHunians():

    root.destroy()

    daftar = Tk()
    daftar.title("Daftar Residen")

    frame = LabelFrame(daftar, text="Data Seluruh Residen", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    opts = LabelFrame(daftar, padx=10, pady=10)
    opts.pack(padx=10, pady=10)

    b_add = Button(opts, text="Add Data", state="disabled")
    b_add.grid(row=0, column=0)

    b_exit = Button(opts, text="Exit", command=daftar.quit)
    b_exit.grid(row=0, column=1)

    for index, h in enumerate(hunians):
        idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)

        type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
        type.grid(row=index, column=1)

        if h.get_jenis() != "Indekos": 
            name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)
        else:
            name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)

        b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
        b_detail.grid(row=index, column=3)

root.mainloop()
