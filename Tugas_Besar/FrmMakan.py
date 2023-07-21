import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Makan import *
class FrmMakan:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("600x390+475+200")
        self.parent.title(title)
        self.parent.resizable(0,0)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        FL = ('Consolas',13)
        Label(mainFrame, text='Kode Makanan\t:', font=FL).place(x=370, y=90)
        Label(mainFrame, text='Porsi\t\t:', font=FL).place(x=370, y=150)
        # Textbox
        self.txtIDMakanan = Entry(mainFrame, width=5) 
        self.txtIDMakanan.place(x=535, y=95)
        self.txtTotal = Entry(mainFrame, width=5) 
        self.txtTotal.place(x=535, y=155)
        # Button
        self.btnPesan = Button(mainFrame, text='Pesan', command=self.Pesan, width=10)
        self.btnPesan.place(x=420, y=220)
        # define columns
        columns = ('ID','IDMakanan','NamaMakanan','Harga')
        self.tree = ttk.Treeview(mainFrame, height=16, columns=columns, show='headings')
        # define headings
        self.tree.heading('ID', text='ID')
        self.tree.column('ID', width="30")
        self.tree.heading('IDMakanan', text='Kode Makanan')
        self.tree.column('IDMakanan', width="100")
        self.tree.heading('NamaMakanan', text='Nama Makanan')
        self.tree.column('NamaMakanan', width="130")
        self.tree.heading('Harga', text='Harga')
        self.tree.column('Harga', width="60")
        # set tree position
        self.tree.place(x=0, y=0)
        
    def onClear(self, event=None):
        self.txtIDMakanan.delete(0,END)
        self.txtIDMakanan.insert(END,"")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data makan
        obj = Makan()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["ID"],d["IDMakanan"],d["NamaMakanan"],d["Harga"]))
    def onCari(self, event=None):
        IDMakanan = self.txtIDMakanan.get()
        obj = Makan()
        a = obj.get_by_IDMakanan(IDMakanan)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        IDMakanan = self.txtIDMakanan.get()
        obj = Makan()
        res = obj.get_by_IDMakanan(IDMakanan)
        self.txtIDMakanan.delete(0,END)
        self.txtIDMakanan.insert(END,obj.IDMakanan)

    def Pesan(self, event=None):
        IDMakanan = self.txtIDMakanan.get()
        Porsi = self.txtTotal.get()
        obj = Makan()
        a = obj.get_by_IDMakanan(IDMakanan)
        Makanan = obj.NamaMakanan
        if(len(a)>0):
            pesanan = Porsi+' '+Makanan
            messagebox.showinfo("Pesanan Dibuat", pesanan+ " Segera diantar")
            self.onKeluar()
                 
    def onSimpan(self, event=None):
        # get the data from input
        IDMakanan = self.txtIDMakanan.get()
        # create new Object
        obj = Makan()
        obj.IDMakanan = IDMakanan
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_IDMakanan(IDMakanan)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        IDMakanan = self.txtIDMakanan.get()
        obj = Makan()
        obj.IDMakanan = IDMakanan
        if(self.ditemukan==True):
            res = obj.delete_by_IDMakanan(IDMakanan)
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
    aplikasi = FrmMakan(root2, "Aplikasi Data Makan")
    root2.mainloop()
