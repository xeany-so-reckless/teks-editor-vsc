import tkinter as tkr
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

import os
from tkinter.messagebox import askokcancel

root = tkr.Tk()

# berfungsi untuk meletakkan tombol-tombol yang kita buat
class SimpleEditor(tkr.Frame):
    def __init__(self, parent=None, file=None):
        tkr.Frame.__init__(self, parent)
        self.frm = tkr.Frame(parent)
        self.frm.pack(fill=tkr.X)
        self.layoutKolom = tkr.Frame(root)
        self.buatNamaFile()
        parent.title("Text Editor by Ahmad Khotibul Umam")
        self.buatTombol()
        self.kolomTeksUtama()
        self.indeks = 1.0
        self.path = ''

# Supaya tombol bekerja Open, Save, dan Exit. Kita memanggil fungsi dengan command=self.openFile dan seterusnya.
# Kemudian kita akan mengatur tata letak tombol itu pada posisi sebelah kiri dengan .pack(side=tkr.LEFT.
    def buatTombol(self):
        tkr.Button(self.frm, text='Open', command=self.openFile).pack(side=tkr.LEFT)
        tkr.Button(self.frm, text='Save', command=self.perintahSimpan).pack(side=tkr.LEFT)
        tkr.Button(self.frm, text='Exit', command=self.perintahKeluar).pack(side=tkr.LEFT)

# Fungsi ini kolomTeksUtama, wadah teks yang diketik (dibuat) dan menggunakan style SUNKEN pada bagian tempat mengetiknya. Kalian bisa menggunakan style lainnya seperti RAISED, GROOVE, RIDGE, atau FLAT. Pilih saja sesuai selera.
    def kolomTeksUtama(self):
        scroll = tkr.Scrollbar(self)
        kolomTeks = tkr.Text(self, relief=tkr.SUNKEN)
        scroll.config(command=kolomTeks.yview)
        kolomTeks.config(yscrollcommand=scroll.set)
        scroll.pack(side=tkr.RIGHT, fill=tkr.Y)
        kolomTeks.pack(side=tkr.LEFT, expand=tkr.YES, fill=tkr.BOTH)
        self.kolomTeks = kolomTeks
        self.pack(expand=tkr.YES, fill=tkr.BOTH)

    # perintah simpan
    def perintahSimpan(self):
        print(self.path)
        if self.path:
            alltext = self.gettext()
            open(self.path, 'w').write(alltext)
            messagebox.showinfo('Berhasil', 'file telah disimpan')
        else:
            tipeFile = [('Text File', '*.txt'), ('Python file', '*.py'),('All files','.*')]
            filename = asksaveasfilename(filetypes=(tipeFile))
            if filename:
                alltext = self.gettext()
                open(filename, 'w').write(alltext)
                self.path = filename

    # perintah keluar aplikasi
    def perintahKeluar(self):
        ans = askokcancel('Exit', 'Anda yakin mau keluar?')
        if ans:
            tkr.Frame.quit(self)

    def settext(self, text='', file=None):
        if file:
            text = open(file, 'r').read()
        self.kolomTeks.delete('1.0', tkr.END)
        self.kolomTeks.insert('1.0', text)
        self.kolomTeks.mark_set(tkr.INSERT, '1.0')
        self.kolomTeks.focus()
    
    def gettext(self):
        return self.kolomTeks.get('1.0', tkr.END+'-1c')
    
    def buatNamaFile(self):
        self.layoutKolom.pack(fill=tkr.BOTH, expand=1, padx=17, pady=5)

# Berikutnya perintah untuk membuka file, ekstensi file yang bisa dibuka semuanya. Ditentukan pada variabel ekstensiFile
    def openFile(self):
        ekstensiFile = [('All files', '*.*'), ('Text Files', '*.txt'), ('Python files', '*.py')]
        open = filedialog.askopenfilename(filetypes = ekstensiFile)
        if open != '':
            text = self.readFile(open)
            if text:
                self.path = open
                #nama = os.path.basename(open)
                self.kolomTeks.delete('0.1', tkr.END)
                self.kolomTeks.insert(tkr.END, text)

# Setelah program berhasil membuka file, perlu dapat melakukan membaca file yang dibuka tadi dan mengembalikan teksnya ke kolomTeks
    def readFile(self, filename):
        try:
            f = open(filename, 'r')
            text = f.read()
            return text
        except:
            messagebox.showerror('Error!')
            return None
        
SimpleEditor(root)
tkr.mainloop()
