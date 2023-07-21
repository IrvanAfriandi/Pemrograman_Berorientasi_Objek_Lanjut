
import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Kamar import *
class FrmKamar:
    
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
        # define columns
        columns = ('IDKamar','KelasKamar','HargaPerMalam','StatusKamar','Penyewa','CheckIN')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('IDKamar', text='IDKAMAR')
        self.tree.column('IDKamar', width="30")
        self.tree.heading('KelasKamar', text='KELASKAMAR')
        self.tree.column('KelasKamar', width="30")
        self.tree.heading('HargaPerMalam', text='HARGAPERMALAM')
        self.tree.column('HargaPerMalam', width="30")
        self.tree.heading('StatusKamar', text='STATUSKAMAR')
        self.tree.column('StatusKamar', width="30")
        self.tree.heading('Penyewa', text='PENYEWA')
        self.tree.column('Penyewa', width="30")
        self.tree.heading('CheckIN', text='CHECKIN')
        self.tree.column('CheckIN', width="30")
        # set tree position
        self.tree.place(x=0, y=200)

    def onReload(self, event=None):
        # get data kamar
        obj = Kamar()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["IDKamar"],d["KelasKamar"],d["HargaPerMalam"],d["StatusKamar"],d["Penyewa"],d["CheckIN"]))

    def onDelete(self, event=None):
        IDKamar = self.txtIDKamar.get()
        obj = Kamar()
        obj.IDKamar = IDKamar
        if(self.ditemukan==True):
            res = obj.delete_by_IDKamar(IDKamar)
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
    aplikasi = FrmKamar(root2, "Aplikasi Data Kamar")
    root2.mainloop()
