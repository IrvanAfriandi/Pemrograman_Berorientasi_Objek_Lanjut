import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Pesanan import *
class FrmPesanan:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='NOPESANAN:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='PEMESAN:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='BARANG:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KUANTITAS:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TOTALHARGA:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtNoPesanan = Entry(mainFrame) 
        self.txtNoPesanan.grid(row=0, column=1, padx=5, pady=5)
        self.txtNoPesanan.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtPemesan = Entry(mainFrame) 
        self.txtPemesan.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtBarang = Entry(mainFrame) 
        self.txtBarang.grid(row=2, column=1, padx=5, pady=5)
        # Textbox
        self.txtKuantitas = Entry(mainFrame) 
        self.txtKuantitas.grid(row=3, column=1, padx=5, pady=5)
        # Textbox
        self.txtTotalHarga = Entry(mainFrame) 
        self.txtTotalHarga.grid(row=4, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('ID','NoPesanan','Pemesan','Barang','Kuantitas','TotalHarga')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('ID', text='ID')
        self.tree.column('ID', width="30")
        self.tree.heading('NoPesanan', text='NOPESANAN')
        self.tree.column('NoPesanan', width="30")
        self.tree.heading('Pemesan', text='PEMESAN')
        self.tree.column('Pemesan', width="30")
        self.tree.heading('Barang', text='BARANG')
        self.tree.column('Barang', width="30")
        self.tree.heading('Kuantitas', text='KUANTITAS')
        self.tree.column('Kuantitas', width="30")
        self.tree.heading('TotalHarga', text='TOTALHARGA')
        self.tree.column('TotalHarga', width="30")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtNoPesanan.delete(0,END)
        self.txtNoPesanan.insert(END,"")
        self.txtPemesan.delete(0,END)
        self.txtPemesan.insert(END,"")
        self.txtBarang.delete(0,END)
        self.txtBarang.insert(END,"")
        self.txtKuantitas.delete(0,END)
        self.txtKuantitas.insert(END,"")
        self.txtTotalHarga.delete(0,END)
        self.txtTotalHarga.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data pesanan
        obj = Pesanan()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["ID"],d["NoPesanan"],d["Pemesan"],d["Barang"],d["Kuantitas"],d["TotalHarga"]))
    def onCari(self, event=None):
        NoPesanan = self.txtNoPesanan.get()
        obj = Pesanan()
        a = obj.get_by_NoPesanan(NoPesanan)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        NoPesanan = self.txtNoPesanan.get()
        obj = Pesanan()
        res = obj.get_by_NoPesanan(NoPesanan)
        self.txtNoPesanan.delete(0,END)
        self.txtNoPesanan.insert(END,obj.NoPesanan)
        self.txtPemesan.delete(0,END)
        self.txtPemesan.insert(END,obj.Pemesan)
        self.txtBarang.delete(0,END)
        self.txtBarang.insert(END,obj.Barang)
        self.txtKuantitas.delete(0,END)
        self.txtKuantitas.insert(END,obj.Kuantitas)
        self.txtTotalHarga.delete(0,END)
        self.txtTotalHarga.insert(END,obj.TotalHarga)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        NoPesanan = self.txtNoPesanan.get()
        Pemesan = self.txtPemesan.get()
        Barang = self.txtBarang.get()
        Kuantitas = self.txtKuantitas.get()
        TotalHarga = self.txtTotalHarga.get()
        # create new Object
        obj = Pesanan()
        obj.NoPesanan = NoPesanan
        obj.Pemesan = Pemesan
        obj.Barang = Barang
        obj.Kuantitas = Kuantitas
        obj.TotalHarga = TotalHarga
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_NoPesanan(NoPesanan)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        NoPesanan = self.txtNoPesanan.get()
        obj = Pesanan()
        obj.NoPesanan = NoPesanan
        if(self.ditemukan==True):
            res = obj.delete_by_NoPesanan(NoPesanan)
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        
        self.onClear()
            
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root2 = tk.Tk()
    aplikasi = FrmPesanan(root2, "Aplikasi Data Pesanan")
    root2.mainloop()
