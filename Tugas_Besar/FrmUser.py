# Script Generated Using PyAthlon
# Create By Freddy Wicaksono, M.Kom
# =================================
# Nama File : FrmUserlog.py
import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Userlog import *
class FrmUserlog:
    
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
        Label(mainFrame, text='NOMORTELEPON:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NAMA:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='EMAIL:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JENISKELAMIN:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KATASANDI:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ROLENAME:').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ALAMAT:').grid(row=6, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtNomorTelepon = Entry(mainFrame) 
        self.txtNomorTelepon.grid(row=0, column=1, padx=5, pady=5)
        self.txtNomorTelepon.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtNama = Entry(mainFrame) 
        self.txtNama.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtEmail = Entry(mainFrame) 
        self.txtEmail.grid(row=2, column=1, padx=5, pady=5)
        # Combo Box
        self.txtJenisKelamin = StringVar()
        Cbo_JenisKelamin = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtJenisKelamin) 
        Cbo_JenisKelamin.grid(row=3, column=1, padx=5, pady=5)
        # Adding JenisKelamin combobox drop down list
        Cbo_JenisKelamin['values'] = ('Laki-Laki','Perempuan')
        Cbo_JenisKelamin.current()
        # Textbox
        self.txtKataSandi = Entry(mainFrame) 
        self.txtKataSandi.grid(row=4, column=1, padx=5, pady=5)
        # Combo Box
        self.txtRolename = StringVar()
        Cbo_Rolename = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtRolename) 
        Cbo_Rolename.grid(row=5, column=1, padx=5, pady=5)
        # Adding Rolename combobox drop down list
        Cbo_Rolename['values'] = ('Tamu','Petugas')
        Cbo_Rolename.current()
        # Textbox
        self.txtAlamat = Entry(mainFrame) 
        self.txtAlamat.grid(row=6, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('ID','NomorTelepon','Nama','Email','JenisKelamin','KataSandi','Rolename','Alamat')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('ID', text='ID')
        self.tree.column('ID', width="30")
        self.tree.heading('NomorTelepon', text='NOMORTELEPON')
        self.tree.column('NomorTelepon', width="30")
        self.tree.heading('Nama', text='NAMA')
        self.tree.column('Nama', width="30")
        self.tree.heading('Email', text='EMAIL')
        self.tree.column('Email', width="30")
        self.tree.heading('JenisKelamin', text='JENISKELAMIN')
        self.tree.column('JenisKelamin', width="30")
        self.tree.heading('KataSandi', text='KATASANDI')
        self.tree.column('KataSandi', width="30")
        self.tree.heading('Rolename', text='ROLENAME')
        self.tree.column('Rolename', width="30")
        self.tree.heading('Alamat', text='ALAMAT')
        self.tree.column('Alamat', width="30")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtNomorTelepon.delete(0,END)
        self.txtNomorTelepon.insert(END,"")
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,"")
        self.txtEmail.delete(0,END)
        self.txtEmail.insert(END,"")
        self.txtJenisKelamin.set("")
        self.txtKataSandi.delete(0,END)
        self.txtKataSandi.insert(END,"")
        self.txtRolename.set("")
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data userlog
        obj = Userlog()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["ID"],d["NomorTelepon"],d["Nama"],d["Email"],d["JenisKelamin"],d["KataSandi"],d["Rolename"],d["Alamat"]))
    def onCari(self, event=None):
        NomorTelepon = self.txtNomorTelepon.get()
        obj = Userlog()
        a = obj.get_by_NomorTelepon(NomorTelepon)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        NomorTelepon = self.txtNomorTelepon.get()
        obj = Userlog()
        res = obj.get_by_NomorTelepon(NomorTelepon)
        self.txtNomorTelepon.delete(0,END)
        self.txtNomorTelepon.insert(END,obj.NomorTelepon)
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,obj.Nama)
        self.txtEmail.delete(0,END)
        self.txtEmail.insert(END,obj.Email)
        self.txtJenisKelamin.set(obj.JenisKelamin)
        self.txtKataSandi.delete(0,END)
        self.txtKataSandi.insert(END,obj.KataSandi)
        self.txtRolename.set(obj.Rolename)
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,obj.Alamat)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        NomorTelepon = self.txtNomorTelepon.get()
        Nama = self.txtNama.get()
        Email = self.txtEmail.get()
        JenisKelamin = self.txtJenisKelamin.get()
        KataSandi = self.txtKataSandi.get()
        Rolename = self.txtRolename.get()
        Alamat = self.txtAlamat.get()
        # create new Object
        obj = Userlog()
        obj.NomorTelepon = NomorTelepon
        obj.Nama = Nama
        obj.Email = Email
        obj.JenisKelamin = JenisKelamin
        obj.KataSandi = KataSandi
        obj.Rolename = Rolename
        obj.Alamat = Alamat
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_NomorTelepon(NomorTelepon)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        NomorTelepon = self.txtNomorTelepon.get()
        obj = Userlog()
        obj.NomorTelepon = NomorTelepon
        if(self.ditemukan==True):
            res = obj.delete_by_NomorTelepon(NomorTelepon)
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
    aplikasi = FrmUserlog(root2, "Aplikasi Data Userlog")
    root2.mainloop()
